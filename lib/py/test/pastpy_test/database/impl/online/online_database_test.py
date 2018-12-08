import os.path
from pastpy.database.impl.online.online_database import OnlineDatabase
from pastpy.gen.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration
from pastpy_test.database._database_test import _DatabaseTest


class OnlineDatabaseTest(_DatabaseTest):
    def setUp(self):
        self._database = \
            OnlineDatabase(configuration=
                OnlineDatabaseConfiguration.builder()
                    .set_download_dir_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', 'devdata', 'tcmuseum')))
                    .set_collection_name('Test').build())
