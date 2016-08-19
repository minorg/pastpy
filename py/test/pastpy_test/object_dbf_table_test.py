import os.path
import unittest

from pastpy.object_dbf_table import ObjectDbfTable


class ObjectDbfTableTest(unittest.TestCase):
    def __open(self):
        dbf_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'devdata', 'buffalostate', 'ftt', 'PPSdata_objects.dbf'))
        return ObjectDbfTable.open(dbf_file_path)

    def test_open(self):
        self.__open()

    def test_records(self):
        for record in self.__open().records():
            pass
#             print record
#             print
#             assert isinstance(record, Object)

