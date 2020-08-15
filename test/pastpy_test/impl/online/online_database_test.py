from pastpy.impl.online.online_database import OnlineDatabase
from pastpy_test._database_test import _DatabaseTest
from pastpy_test.test_database_configurations import TestDatabaseConfigurations


class OnlineDatabaseTest(_DatabaseTest):
    def setUp(self):
        if TestDatabaseConfigurations.ONLINE is not None:
            self._database = OnlineDatabase(configuration=TestDatabaseConfigurations.ONLINE)