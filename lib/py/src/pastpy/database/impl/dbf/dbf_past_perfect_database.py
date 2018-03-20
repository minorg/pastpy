import os.path
from pastpy.database.past_perfect_database import PastPerfectDatabase
from pastpy.database.impl.dbf.objects_dbf_table import ObjectsDbfTable
from pastpy.database.impl.dbf.dbf_object import DbfObject


class DbfPastPerfectDatabase(PastPerfectDatabase):
    def __init__(self, *, pp_images_dir_path=None, pp_install_dir_path=None, pp_objects_dbf_file_path=None):
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
        elif pp_objects_dbf_file_path is None:
            raise ValueError(
                "must specify a PastPerfect installation directory or an objects DBF file")
        self.__pp_images_dir_path = pp_images_dir_path
        self.__pp_objects_dbf_file_path = pp_objects_dbf_file_path

    def objects(self):
        with ObjectsDbfTable.open(self.__pp_objects_dbf_file_path) as table:
            for record in table.records():
                yield DbfObject(images_dir_path=self.__pp_images_dir_path, record=record)
