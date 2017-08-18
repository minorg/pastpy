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
        pp_images_dir_path=None,
        pp_install_dir_path=None,
        pp_objects_dbf_file_path=None,
        template_dir_path=None
    ):
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)
        self.__output_dir_path = output_dir_path

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

    @classmethod
    def main(cls):
        from argparse import ArgumentParser

        pp_dir_path_example = 'C:\\pp5'
        argument_parser = ArgumentParser()
        argument_parser.add_argument('-i', '--pp', dest='pp_install_dir_path',
                                     help='Path to the PastPerfect 5 installation directory e.g., %(pp_dir_path_example)s' % locals())
        argument_parser.add_argument(
            '-o', dest='output_dir_path', help="Path to the output directory")
        argument_parser.add_argument('--images', dest='pp_images_dir_path',
                                     help='Path to the PastPerfect 5 images directory e.g., %(pp_dir_path_example)s\\Images' % locals())
        argument_parser.add_argument('--objects-dbf', dest='pp_objects_dbf_file_path',
                                     help='Path to the PastPerfect 5 objects DBF file e.g., %(pp_dir_path_example)s\\Data\\OBJECTS.DBF for all objects or an objects export for a subset' % locals())
        argument_parser.add_argument(
            '-t', '--template', dest='template_dir_path', help="Path to the templates directory, defaults to " + cls.TEMPLATE_DIR_PATH_DEFAULT)
        args = argument_parser.parse_args()

        try:
            inst = \
                cls(
                    output_dir_path=args.output_dir_path,
                    pp_images_dir_path=args.pp_images_dir_path,
                    pp_install_dir_path=args.pp_install_dir_path,
                    pp_objects_dbf_file_path=args.pp_objects_dbf_file_path,
                    template_dir_path=args.template_dir_path
                )
        except ValueError as e:
            print("Error: " + str(e) + "\n\n", file=sys.stderr)
            argument_parser.print_help()
            sys.exit(1)

        inst.generate()

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
        rendered = self.__renderer.render_name(file_base_name + '.html')
        out_file_path = os.path.join(
            self.__output_dir_path, file_base_name + '.html')
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            logging.info("wrote %s", out_file_path)

    def __render_index(self):
        self.__render_file('index', {})

    def __render_objects(self):
        objects = self.__read_objects()


if __name__ == '__main__':
    SiteGenerator.main()
