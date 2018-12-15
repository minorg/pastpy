import os.path
from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.gen.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class TestDatabaseConfigurations(object):
    DBF = DbfDatabaseConfiguration.builder()\
        .set_pp_objects_dbf_file_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'devdata', 'buffalostate', 'ftt', 'PPSdata_Objects.dbf')))\
        .set_pp_images_dir_path(".").build()

    ONLINE = OnlineDatabaseConfiguration.builder()\
        .set_download_dir_path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..', 'devdata', 'tcmuseum')))\
        .set_collection_name('Test').build()
