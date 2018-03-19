import logging
import os.path
import pystache
import shutil
import sys
from urllib.parse import urlparse, unquote

try:
    __import__('pastpy')
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'lib', 'py', 'src')))
    __import__('pastpy')
from pastpy.object_dbf_table import ObjectDbfTable


class SiteGenerator(object):
    COPYRIGHT_HOLDER_DEFAULT = 'Your Collection'
    SITE_NAME_DEFAULT = 'Your Collection'

    PP_INSTALL_DIR_PATH_EXAMPLE = "C:\\pp5"
    PP_IMAGES_DIR_PATH_EXAMPLE = os.path.join(
        PP_INSTALL_DIR_PATH_EXAMPLE, 'Images')
    PP_REPORTS_DIR_PATH_EXAMPLE = "C:\\pp5Reports"

    TEMPLATE_DIR_PATH_DEFAULT = \
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), '..', '..', 'mustache'))
    assert os.path.isdir(TEMPLATE_DIR_PATH_DEFAULT), TEMPLATE_DIR_PATH_DEFAULT

    class ObjectWrapper(object):
        def __init__(self, img_srcs, object_):
            self.__img_srcs = img_srcs
            self.__object = object_

        def __getattr__(self, attr):
            return getattr(self.__object, attr)

        @property
        def img_srcs(self):
            return self.__img_srcs

    def __init__(
        self,
        database,
        output_dir_path,
        copyright_holder=None,
        site_name=None,
        template_dir_path=None
    ):
        self.__database = database
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)
        self.__output_dir_path = output_dir_path

        self.__copyright_holder = copyright_holder if copyright_holder is not None else self.COPYRIGHT_HOLDER_DEFAULT

        self.__site_name = site_name if site_name is not None else self.SITE_NAME_DEFAULT

        if template_dir_path is None:
            template_dir_path = self.TEMPLATE_DIR_PATH_DEFAULT
        if not os.path.isdir(template_dir_path):
            raise ValueError(
                "template directory %s does not exist" % template_dir_path)

        self.__renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(template_dir_path,)
            )

    def generate(self):
        if not os.path.isdir(self.__output_dir_path):
            os.makedirs(self.__output_dir_path)
            self.__logger.info("created output directory %s",
                               self.__output_dir_path)

        objects = self.__read_objects()

        self.__render_index()
        self.__render_objects_master(objects=objects)
        self.__render_objects_detail(objects=objects)

    def __new_context(self, page_title):
        return {'copyright_holder': self.__copyright_holder, 'page_title': page_title, 'site_name': self.__site_name}

    def __read_objects(self):
        out_images_dir_path = os.path.join(self.__output_dir_path, 'img')
        if not os.path.isdir(out_images_dir_path):
            os.makedirs(out_images_dir_path)
            self.__logger.info(
                "created output images directory %s", out_images_dir_path)

        objects = []
        for object_ in self.__database.objects():
            img_srcs = []
            for image in object_.images:
                full_size_url = image.full_size_url
                full_size_url_parsed = urlparse(full_size_url)
                if full_size_url_parsed.scheme == "file":
                    full_size_file_path = unquote(full_size_url)[7:]
                    full_size_file_name = os.path.split(full_size_file_path)[1]
                    out_image_file_path = os.path.join(
                        out_images_dir_path, full_size_file_name)
                    shutil.copyfile(full_size_file_path,
                                    full_size_file_name)
                    self.__logger.info(
                        "copied %s to %s", full_size_file_path, out_image_file_path)
                    img_srcs.append('img/' + full_size_file_name)
            objects.append(SiteGenerator.ObjectWrapper(
                img_srcs=tuple(img_srcs),
                object_=object_
            ))
            break
        return objects

    def __render_file(self, file_base_name, context, out_file_relpath=None):
        rendered = self.__renderer.render_name(
            file_base_name + '.html', context)
        if out_file_relpath is None:
            out_file_relpath = file_base_name + '.html'
        out_file_path = os.path.join(
            self.__output_dir_path, out_file_relpath)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            logging.info("wrote %s", out_file_path)

    def __render_index(self):
        context = self.__new_context(page_title='Home')
        self.__render_file('index', context)

    def __render_objects_master(self, objects):
        context = self.__new_context(page_title='Objects')
        self.__render_file('objects_master', context)

    def __render_objects_detail(self, objects):
        out_dir_path = os.path.join(self.__output_dir_path, 'objects')
        if not os.path.isdir(out_dir_path):
            os.makedirs(out_dir_path)

        for object_ in objects:
            if not object_.id:
                continue
            context = self.__new_context(
                page_title='Object: ' + object_.id)
            self.__render_file('object_detail', context, out_file_relpath=os.path.join(
                'objects', object_.id + '.html'))
