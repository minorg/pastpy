from pastpy.database.impl.online.online_database import OnlineDatabase
from pastpy_test.database._database_test import _DatabaseTest
from pastpy_test.database.test_database_configurations import TestDatabaseConfigurations


class OnlineDatabaseTest(_DatabaseTest):
    def setUp(self):
        self._database = OnlineDatabase(configuration=TestDatabaseConfigurations.ONLINE)
