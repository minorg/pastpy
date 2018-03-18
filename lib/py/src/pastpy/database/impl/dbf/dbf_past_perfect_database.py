import os.path
from pastpy.past_perfect_database import PastPerfectDatabase
from pastpy.database.impl.dbf.objects_dbf_table import ObjectsDbfTable
from pastpy.database.impl.dbf.dbf_object import DbfObject


class DbfPastPerfectDatabase(PastPerfectDatabase):
    def __init__(self, pp_install_dir_path):
        self.__pp_install_dir_path = pp_install_dir_path

    def objects(self):
        with ObjectsDbfTable.open(os.path.join(self.__data_dir_path, "Data", "OBJECTS.DBF")) as table:
            for record in table.records():
                yield DbfObject(record)
