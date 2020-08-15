from pastpy.impl.dummy.dummy_database import DummyDatabase
from pastpy_test.database._database_test import _DatabaseTest
from pastpy_test.database.test_database_configurations import TestDatabaseConfigurations


class DummyDatabaseTest(_DatabaseTest):
    def setUp(self):
        self._database = \
            DummyDatabase(configuration=TestDatabaseConfigurations.DUMMY)

    def test_objects(self):
        self._test_objects()
