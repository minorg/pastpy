import inspect
import json
import logging
import os.path
import re
import shutil
from urllib.parse import unquote, urlparse
from xml.sax import saxutils

from pastpy.gen.name_value_pair import NameValuePair
from pastpy.gen.site.site_image import SiteImage
from pastpy.gen.site.site_object import SiteObject


class SiteObjectsReader(object):
    def __init__(self, *, configuration, database):
        self.__configuration = configuration
        self.__database = database
        self.__logger = logging.getLogger(SiteObjectsReader.__class__.__name__)

    def __copy_file_url(self, source_file_url, dest_dir_path):
        if not source_file_url:
            return None, None
        source_file_url_parsed = urlparse(source_file_url)
        if source_file_url_parsed.scheme != "file":
            return source_file_url, None
        source_file_path = unquote(source_file_url)[8:].replace('/', os.path.sep)
        assert os.path.isfile(source_file_path), source_file_path
        source_file_name = os.path.split(
            source_file_path)[1]
        dest_file_path = os.path.join(
            dest_dir_path, source_file_name)
        self.__makedirs(dest_dir_path)
        shutil.copyfile(source_file_path,
                        dest_file_path)
        self.__logger.debug(
            "copied %s to %s", source_file_path, dest_file_path)
        dest_file_url = os.path.relpath(
            dest_file_path, self.__configuration.output_dir_path).replace(os.path.sep, '/')
        return dest_file_path, dest_file_url

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.debug("created directory %s", dir_path)

    def read_objects(self):

        object_ids_by_file_name = {}
        objects = []
        for database_object in self.__database.objects():
            if not database_object.id:
                self.__logger.warn("database object has no id")
                continue

            images = []
            out_images_dir_path = os.path.join(
                self.__configuration.output_dir_path, 'img')
            out_full_size_images_dir_path = os.path.join(
                out_images_dir_path, "full_size")
            out_thumbnail_images_dir_path = os.path.join(
                out_images_dir_path, "thumbnail")
            for database_image in database_object.images:
                full_size_url, full_size_file_path = self.__copy_file_url(
                    database_image.full_size_url, out_full_size_images_dir_path)

                thumbnail_url, _thumbnail_file_path = self.__copy_file_url(
                    database_image.thumbnail_url, out_thumbnail_images_dir_path)
                if not thumbnail_url and full_size_file_path:
                    thumbnail_url = full_size_url
                    # raise NotImplementedError("shrink here")

                if full_size_url or thumbnail_url:
                    images.append(SiteImage(
                        full_size_url=full_size_url,
                        thumbnail_url=thumbnail_url,
                        title=database_image.title
                    ))

            file_name = self.__to_valid_filename(database_object.id) + ".html"
            existing_object_id = object_ids_by_file_name.get(file_name)
            if existing_object_id is not None:
                raise RuntimeError("two objects (%s and %s) map to the same file name (%s)" % (
                    existing_object_id, database_object.id, file_name))
            object_ids_by_file_name[file_name] = database_object.id

            object_builder = SiteObject.builder()

            object_builder.absolute_href = "/objects/details/" + file_name
            object_builder.file_name = file_name

            object_builder.full_size_images = \
                tuple(image for image in images if image.full_size_url)
            object_builder.thumbnail_images = \
                tuple(image for image in images if image.thumbnail_url)
            object_builder.has_full_size_images = len(
                object_builder.full_size_images) > 0
            object_builder.has_thumbnail_images = len(
                object_builder.thumbnail_images) > 0
            if object_builder.thumbnail_images:
                object_builder.thumbnail_url = object_builder.thumbnail_images[0].thumbnail_url
            else:
                object_builder.thumbnail_url = "http://via.placeholder.com/210x211?text=Missing%20image"

            object_builder.impl_attributes_list = \
                tuple(NameValuePair(name=name, value=value)
                      for name, value in database_object.impl_attributes.items())

            if database_object.name:
                object_builder.name = database_object.name
            elif database_object.othername:
                object_builder.name = database_object.othername
            else:
                object_builder.name = database_object.id

            standard_attributes_map = {}
            standard_attributes_map_json = {}
            standard_attributes_map_xml = {}
            for member_name, member in inspect.getmembers(database_object):
                if inspect.ismethod(member):
                    continue
                if member_name.startswith('_'):
                    continue
                elif member_name in ("images", "impl_attributes"):
                    continue
                value = getattr(database_object, member_name)
                if value is not None:
                    standard_attributes_map[member_name] = value
                    standard_attributes_map_json[member_name] = json.dumps(
                        value)
                    standard_attributes_map_xml[member_name] = saxutils.escape(
                        value)
                else:
                    standard_attributes_map_json[member_name] = ''
                    standard_attributes_map_xml[member_name] = ''
            object_builder.standard_attributes_list = \
                tuple(NameValuePair(name=name, value=value)
                      for name, value in standard_attributes_map.items())
            object_builder.standard_attributes_list_xml = tuple(NameValuePair(
                key, value) for key, value in standard_attributes_map_xml.items())
            object_builder.standard_attributes_map = standard_attributes_map
            object_builder.standard_attributes_map_json = standard_attributes_map_json
            for name, value in standard_attributes_map.items():
                setattr(object_builder, name, value)

            if object_builder.title is None:
                object_builder.title = object_builder.name

            objects.append(object_builder.build())
            if len(objects) == 100:
                break
        return objects

    @staticmethod
    def __to_valid_filename(s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)
