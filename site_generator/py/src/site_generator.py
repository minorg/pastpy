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
        pp_install_dir_path,
        template_dir_path=None
    ):
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)
        self.__output_dir_path = output_dir_path
        if not os.path.isdir(pp_install_dir_path):
            raise ValueError(
                "PastPerfect installation directory %s does not exist" % pp_install_dir_path)
        self.__pp_install_dir_path = pp_install_dir_path
        if template_dir_path is None:
            template_dir_path = \
                os.path.abspath(os.path.join(
                    os.path.dirname(__file__), '..', '..', 'mustache'))
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

    @classmethod
    def main(cls):
        from argparse import ArgumentParser

        argument_parser = ArgumentParser()
        argument_parser.add_argument('-i', '--pp', dest='pp_install_dir_path',
                                     help='Path to the PastPerfect 5 installation directory e.g., C:\pp5eval')
        argument_parser.add_argument(
            '-o', '--out', dest='output_dir_path', help="Path to the output directory")
        argument_parser.add_argument(
            '-t', '--template', dest='template_dir_path', help="Path to the templates directory")
        args = argument_parser.parse_args()

        cls(
            output_dir_path=args.output_dir_path,
            pp_install_dir_path=args.pp_install_dir_path,
            template_dir_path=args.template_dir_path
        ).generate()

    def __read_objects(self):
        pp_images_dir_path = os.path.join(
            self.__pp_install_dir_path, 'Images', '001')
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
        with ObjectDbfTable.open(os.path.join(self.__pp_install_dir_path, 'Data', 'OBJECTS.DBF')) as table:
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
        rendered = self.__renderer.render_name(file_base_name + '.html')
        out_file_path = os.path.join(
            self.__output_dir_path, file_base_name + '.html')
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)

    def __render_index(self):
        self.__render_file('index', {})

    def __render_objects(self):
        objects = self.__read_objects()


if __name__ == '__main__':
    SiteGenerator.main()
