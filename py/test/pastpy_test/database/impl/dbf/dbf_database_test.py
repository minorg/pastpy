from pastpy.database.impl.dbf.dbf_database import DbfDatabase
from pastpy_test.database._database_test import _DatabaseTest
from pastpy_test.database.test_database_configurations import TestDatabaseConfigurations


class DbfDatabaseTest(_DatabaseTest):
    def setUp(self):
        self._database = \
            DbfDatabase(configuration=TestDatabaseConfigurations.DBF)