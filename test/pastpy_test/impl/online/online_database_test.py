from pastpy.impl.online.online_database import OnlineDatabase
from pastpy_test._database_test import _DatabaseTest
from pastpy_test.test_database_configurations import TestDatabaseConfigurations


class OnlineDatabaseTest(_DatabaseTest):
    def setUp(self):
        if TestDatabaseConfigurations.ONLINE is not None:
            self._database = OnlineDatabase(
                configuration=TestDatabaseConfigurations.ONLINE
            )
        else:
            self._database = None

    # def test_download(self):
    #     if self._database is None:
    #         return
    #     self._database.download(tqdm_disable=False)
    #
    # def test_objects(self):
    #     if self._database is None:
    #         return
    #     for object_ in self._database.objects():
    #         print(object_)
    #         for image in object_.images:
    #             print(image)
