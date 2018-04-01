from collections import OrderedDict
from datetime import date, datetime
import logging
import os.path
import re
import shutil
import pystache
import inspect
from urllib.parse import urlparse
from pastpy.gen.site.site_configuration import SiteConfiguration
from pastpy.gen.site.site_image import SiteImage
from pastpy.gen.site.site_index import SiteIndex
from pastpy.gen.site.site_key_value_pair import SiteKeyValuePair
from pastpy.gen.site.site_metadata import SiteMetadata
from pastpy.gen.site.site_nav_items import SiteNavItems
from pastpy.gen.site.site_object import SiteObject
from pastpy.gen.site.site_object_detail import SiteObjectDetail
from pastpy.gen.site.site_objects_list import SiteObjectsList
from pastpy.gen.site.site_objects_list_page_number import SiteObjectsListPageNumber
from pastpy.gen.site.site_sitemap import SiteSitemap


class SiteGenerator(object):
    TEMPLATE_DIR_PATH_DEFAULT = \
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'template'))
    assert os.path.isdir(
        TEMPLATE_DIR_PATH_DEFAULT), TEMPLATE_DIR_PATH_DEFAULT

    def __init__(self, *, configuration, database):
        assert isinstance(configuration, SiteConfiguration)
        self.__database = database
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)

        if configuration.template_dir_path is None:
            configuration = configuration.replacer().set_template_dir_path(
                self.TEMPLATE_DIR_PATH_DEFAULT).build()
        if not os.path.isdir(configuration.template_dir_path):
            raise ValueError(
                "template directory %s does not exist" % configuration.template_dir_path)

        self.__configuration = configuration

        self.__objects = None

        self.__renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(configuration.template_dir_path,)
            )

    def __clean(self):
        self.__rmtree(self.__configuration.output_dir_path)

    def __copy_static_files(self):
        for dir_name in ("css", "js"):
            src_dir_path = os.path.join(
                self.__configuration.template_dir_path, dir_name)
            if os.path.isdir(src_dir_path):
                dst_dir_path = os.path.join(
                    self.__configuration.output_dir_path, dir_name)
                shutil.copytree(src_dir_path, dst_dir_path)
                self.__logger.debug("copied %s to %s",
                                    src_dir_path, dst_dir_path)

    def __filter_objects_with_ids(self, *, objects):
        objects_by_id = OrderedDict()
        for object_ in objects:
            if object_.id:
                if object_.id not in objects_by_id:
                    objects_by_id[object_.id] = object_
                else:
                    self.__logger.warning("duplicate object id: %s", object_)
            else:
                self.__logger.warning("object has no id: %s", object_)
        return objects_by_id.values()

    def generate(self):
        self.__clean()
        self.__makedirs(self.__configuration.output_dir_path)

        self.__copy_static_files()

        self.__read_objects()

        self.__render_index()
        self.__render_object_details()
        objects_list_pages = self.__render_objects_list()
        self.__render_sitemap(objects_list_pages=objects_list_pages)

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.debug("created directory %s", dir_path)

    def __new_metadata(self, *, out_dir_path, active_nav_item="home"):
        builder = SiteMetadata.builder()
        builder.root_relative_href = os.path.relpath(
            self.__configuration.output_dir_path, out_dir_path).replace(os.path.sep, '/')
        builder.configuration = self.__configuration
        builder.current_year = datetime.now().year
        nav_items_builder = SiteNavItems.builder()
        setattr(nav_items_builder, active_nav_item, True)
        builder.nav_items = nav_items_builder.build()
        return builder.build()

    @staticmethod
    def __page_range(*, page_i, page_max, page_min, window):
        assert window / 2 == window // 2, "window must be even"
        start = page_i - window // 2
        end = page_i + window // 2
        # print("First cut")
        # print(start, end)

        if start >= page_min and end <= page_max:
            return range(start, end + 1)

        # print("Adjusting start")

        while start < page_min:
            start = start + 1
            if end < page_max:
                end = end + 1
            # print(start, end)

        # print("Adjusting end")

        while end > page_max:
            end = end - 1
            if start > page_min:
                start = start - 1
            # print(start, end)

        return range(start, end + 1)

    def __read_objects(self):
        out_images_dir_path = os.path.join(
            self.__configuration.output_dir_path, 'img')
        if not os.path.isdir(out_images_dir_path):
            os.makedirs(out_images_dir_path)
            self.__logger.debug(
                "created output images directory %s", out_images_dir_path)

        object_ids_by_file_name = {}
        self.__objects = []
        for database_object in self.__database.objects():
            images = []
            for database_image in database_object.images:
                full_size_url = database_image.full_size_url
                if full_size_url:
                    full_size_url_parsed = urlparse(full_size_url)
                    if full_size_url_parsed.scheme == "file":
                        raise NotImplementedError(
                            "TODO: rewrite the actual image object with a substitute")
                        # full_size_file_path = unquote(full_size_url)[7:]
                        # full_size_file_name = os.path.split(full_size_file_path)[1]
                        # out_image_file_path = os.path.join(
                        #     out_images_dir_path, full_size_file_name)
                        # shutil.copyfile(full_size_file_path,
                        #                 full_size_file_name)
                        # self.__logger.debug(
                        #     "copied %s to %s", full_size_file_path, out_image_file_path)
                        # img_srcs.append('img/' + full_size_file_name)
                images.append(SiteImage(
                    full_size_url=database_image.full_size_url,
                    thumbnail_url=database_image.thumbnail_url,
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
                tuple(image for image in images if image.thumbnail_images)
            object_builder.has_full_size_images = len(
                object_builder.full_size_images) > 0
            object_builder.has_thumbnail_images = len(
                object_builder.thumbnail_images) > 0
            if object_builder.thumbnail_images:
                object_builder.thumbnail_url = object_builder.thumbnail_images[0].thumbnail_url
            else:
                object_builder.thumbnail_url = "http://via.placeholder.com/210x211?text=Missing%20image"

            object_builder.impl_attributes = \
                tuple(SiteKeyValuePair(key=key, value=value)
                      for key, value in database_object.impl_attributes.items())

            if database_object.name:
                object_builder.name = database_object.name
            elif database_object.othername:
                object_builder.name = database_object.othername
            else:
                object_builder.name = database_object.id

            standard_attributes = []
            for member_name, member in inspect.getmembers(database_object):
                if inspect.ismethod(member):
                    continue
                if member_name.startswith('_'):
                    continue
                elif member_name in ("images", "impl_attributes"):
                    continue
                value = getattr(database_object, member_name)
                if value is not None:
                    standard_attributes[member_name] = value
            object_builder.standard_attributes = \
                tuple(SiteKeyValuePair(key=key, value=value)
                      for key, value in standard_attributes.items())
            for key, value in standard_attributes:
                setattr(object_builder, key, value)

            if object_builder.title is None:
                object_builder.title = object_builder.name

            self.__objects.append(object_builder.build())
            if len(self.__objects) == 100:
                break

    def __render_file(self, *, context, file_name, out_file_relpath=None):
        rendered = self.__renderer.render_name(
            file_name, context)
        if out_file_relpath is None:
            out_file_relpath = file_name
        out_file_path = os.path.join(
            self.__configuration.output_dir_path, out_file_relpath)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            self.__logger.debug("wrote %s", out_file_path)

    def __render_index(self):
        context = \
            SiteIndex(
                metadata=self.__new_metadata(
                    active_nav_item="home",
                    out_dir_path=self.__configuration.output_dir_path
                )
            )
        self.__render_file(context=context, file_name='index.html')

    def __render_object_details(self):
        out_dir_relpath = os.path.join('objects', 'details')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        for object_ in self.__objects:
            context = \
                SiteObjectDetail(
                    metadata=self.__new_metadata(
                        active_nav_item="objects",
                        out_dir_path=out_dir_path
                    ),
                    object=object_
                )
            self.__render_file(file_name='object_detail.html', context=context, out_file_relpath=os.path.join(
                out_dir_relpath, context.object.file_name))

    def __render_objects_list(self):
        out_dir_relpath = os.path.join('objects', 'list')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        objects = list(reversed(list(self.__objects)))
        objects_pages = []
        objects_per_page = 20
        while objects:
            objects_page = []
            while objects and len(objects_page) < objects_per_page:
                objects_page.append(objects.pop())
            objects_pages.append(objects_page)

        objects_list_pages = []
        for objects_page_i, objects_page in enumerate(objects_pages):
            # *page_number* is one-based
            # current_page_number = objects_page_i + 1

            out_file_relpath = os.path.join(
                out_dir_relpath, str(objects_page_i + 1) + '.html')

            context_builder = SiteObjectsList.builder()
            context_builder.absolute_href = "/" + \
                out_file_relpath.replace(os.path.sep, '/')
            context_builder.metadata = self.__new_metadata(
                active_nav_item="objects", out_dir_path=out_dir_path)
            context_builder.objects = objects_page

            context_builder.next_page_number = SiteObjectsListPageNumber(
                active=False,
                enabled=objects_page_i + 1 < len(objects_pages),
                number=objects_page_i + 2
            )
            context_builder.previous_page_number = SiteObjectsListPageNumber(
                active=False,
                enabled=objects_page_i > 0,
                number=objects_page_i
            )

            visible_page_numbers = []
            objects_page_range = self.__page_range(
                page_i=objects_page_i, page_min=0, page_max=len(objects_pages) - 1, window=10)
            for objects_page_range_i in objects_page_range:
                visible_page_numbers.append(SiteObjectsListPageNumber(
                    active=objects_page_range_i == objects_page_i,
                    enabled=True,
                    number=objects_page_range_i + 1
                ))
            context_builder.visible_page_numbers = tuple(visible_page_numbers)
            context = context_builder.build()

            self.__render_file(
                file_name='objects_list.html',
                context=context,
                out_file_relpath=out_file_relpath
            )
            objects_list_pages.append(context)
        return objects_list_pages

    def __render_sitemap(self, objects_list_pages):
        context_builder = SiteSitemap.builder()
        context_builder.lastmod = date.today().isoformat()
        context_builder.objects_list_pages = objects_list_pages
        objects = []
        for object_ in self.__objects:
            objects.append(object_.replacer().set_standard_attributes(tuple(
                item for item in object_.standard_attributes
                if item.key != "description"
            )))
        context_builder.objects = tuple(objects)
        context = context_builder.build()

        self.__render_file(file_name='sitemap.xml', context=context)

    def __rmtree(self, dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self.__logger.debug("deleted directory %s", dir_path)

    @staticmethod
    def __to_valid_filename(s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)
