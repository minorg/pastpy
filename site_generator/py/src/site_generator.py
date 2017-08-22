import logging
import os.path
import pystache
import shutil
import sys

try:
    __import__('pastpy')
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', '..', '..', 'lib', 'py', 'src')))
    __import__('pastpy')
from pastpy.models.object_record import ObjectRecord
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

    class ObjectRecordWrapper(object):
        def __init__(self, img_srcs, object_record):
            self.__img_srcs = img_srcs
            self.__object_record = object_record

        def __getattr__(self, attr):
            return getattr(self.__object_record, attr)

        @property
        def img_srcs(self):
            return self.__img_srcs

    def __init__(
        self,
        output_dir_path,
        copyright_holder=None,
        pp_images_dir_path=None,
        pp_install_dir_path=None,
        pp_objects_dbf_file_path=None,
        site_name=None,
        template_dir_path=None
    ):
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)
        self.__output_dir_path = output_dir_path

        self.__copyright_holder = copyright_holder if copyright_holder is not None else self.COPYRIGHT_HOLDER_DEFAULT

        if pp_install_dir_path is not None:
            if not os.path.isdir(pp_install_dir_path):
                raise ValueError(
                    "PastPerfect installation directory %s does not exist" % pp_install_dir_path)
            if pp_images_dir_path is None:
                pp_images_dir_path = os.path.join(
                    pp_install_dir_path, 'Images')
            if pp_objects_dbf_file_path is None:
                pp_objects_dbf_file_path = os.path.join(
                    pp_install_dir_path, 'Data', 'OBJECTS.DBF')
        elif pp_images_dir_path is None:
            raise ValueError(
                "must specify a PastPerfect installation directory or an images directory")
        elif pp_objects_dbf_file_path:
            raise ValueError(
                "must specify a PastPerfect installation directory or an objects DBF file")

        if not os.path.isdir(pp_images_dir_path):
            raise ValueError(
                "PastPErfect images directory %s does not exist" % pp_images_dir_path)
        self.__pp_images_dir_path = pp_images_dir_path

        if not os.path.isfile(pp_objects_dbf_file_path):
            raise ValueError(
                "PastPerfect objects DBF file %s does not exist" % pp_objects_dbf_file_path)
        self.__pp_objects_dbf_file_path = pp_objects_dbf_file_path

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

        self.__render_index()
        self.__render_objects()

    def __new_context(self, page_title):
        return {'copyright_holder': self.__copyright_holder, 'page_title': page_title, 'site_name': self.__site_name}

    def __read_objects(self):
        pp_images_dir_path = os.path.join(self.__pp_images_dir_path, '001')
        if not os.path.isdir(pp_images_dir_path):
            self.__logger.warning(
                "images directory %s does not exist", pp_images_dir_path)
            pp_images_dir_path = None
        out_images_dir_path = os.path.join(self.__output_dir_path, 'img')
        if not os.path.isdir(out_images_dir_path):
            os.makedirs(out_images_dir_path)
            self.__logger.info(
                "created output images directory %s", out_images_dir_path)

        objects = []
        with ObjectDbfTable.open(self.__pp_objects_dbf_file_path) as table:
            for object_record in table.records():
                img_srcs = []
                if pp_images_dir_path is not None and object_record.objectid is not None:
                    pp_image_i = 0
                    while True:
                        pp_image_file_name = object_record.objectid
                        if pp_image_i > 0:
                            pp_image_file_name = pp_image_file_name + \
                                '-' + str(pp_image_i)
                        pp_image_i = pp_image_i + 1
                        pp_image_file_name = pp_image_file_name + '.jpg'
                        pp_image_file_path = os.path.join(
                            pp_images_dir_path, pp_image_file_name)
                        if not os.path.isfile(pp_image_file_path):
                            self.__logger.debug(
                                "object %s image %s does not exist", object_record.objectid, pp_image_file_path)
                            break
                        out_image_file_path = os.path.join(
                            out_images_dir_path, pp_image_file_name)
                        shutil.copyfile(pp_image_file_path,
                                        out_image_file_path)
                        self.__logger.info(
                            "copied %s to %s", pp_image_file_path, out_image_file_path)
                        img_srcs.append('img/' + pp_image_file_name)

                objects.append(SiteGenerator.ObjectRecordWrapper(
                    img_srcs=img_srcs,
                    object_record=object_record
                ))
                break
        return objects

    def __render_file(self, file_base_name, context):
        rendered = self.__renderer.render_name(
            file_base_name + '.html', context)
        out_file_path = os.path.join(
            self.__output_dir_path, file_base_name + '.html')
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            logging.info("wrote %s", out_file_path)

    def __render_index(self):
        context = self.__new_context(page_title='Home')
        self.__render_file('index', context)

    def __render_objects(self):
        objects = self.__read_objects()
