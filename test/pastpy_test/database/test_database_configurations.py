import os.path
from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.gen.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.gen.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class TestDatabaseConfigurations(object):
    DBF = DbfDatabaseConfiguration.builder()\
        .set_pp_objects_dbf_file_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'devdata', 'buffalostate', 'ftt', 'PPSdata_Objects.dbf')))\
        .set_pp_images_dir_path(".").build()

    if not os.path.isfile(DBF.pp_objects_dbf_file_path):
        DBF = None

    DUMMY = DummyDatabaseConfiguration()

    ONLINE = OnlineDatabaseConfiguration.builder()\
        .set_download_dir_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'devdata', 'tcmuseum')))\
        .set_collection_name('Test').build()

    if not os.path.isdir(ONLINE.download_dir_path):
        ONLINE = None
