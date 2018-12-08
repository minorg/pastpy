import os.path
from pastpy.database.impl.dbf.dbf_database import DbfDatabase
from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy_test.database._database_test import _DatabaseTest


class DbfDatabaseTest(_DatabaseTest):
    def setUp(self):
        self._database = \
            DbfDatabase(configuration=
                DbfDatabaseConfiguration.builder()
                    .set_pp_objects_dbf_file_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', '..', '..', '..', 'devdata', 'buffalostate', 'ftt', 'PPSdata_Objects.dbf')))
                    .set_pp_images_dir_path(".").build())
