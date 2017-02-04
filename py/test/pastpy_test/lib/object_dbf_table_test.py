import unittest

from pastpy.lib.models.object_record import ObjectRecord
from pastpy.lib.object_dbf_table import ObjectDbfTable


class ObjectDbfTableTest(unittest.TestCase):
    def __open(self):
        #dbf_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'devdata', 'buffalostate', 'ftt', 'PPSdata_objects.dbf'))
        dbf_file_path = "c:\\pp5eval\\Data\\OBJECTS.DBF"
        return ObjectDbfTable.open(dbf_file_path)

    def test_open(self):
        self.__open()

    def test_records(self):
        records_by_objectid = {}
        for record in self.__open().records():
            assert isinstance(record, ObjectRecord)
            if record.objectid is None:
                continue
            records_by_objectid.setdefault(record.objectid, []).append(record)
        for objectid, records in records_by_objectid.iteritems():  # @UnusedVariable
            for record in records:
                if record.imagefile is not None:
                    print record
