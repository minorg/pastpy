import os.path
from pathlib import Path

from pastpy.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class TestDatabaseConfigurations:
    DBF = \
        DbfDatabaseConfiguration(
            pp_objects_dbf_file_path=Path(__file__).parent.parent.parent / 'devdata' / 'buffalostate' / 'ftt' / 'PPSdata_Objects.dbf',
            pp_images_dir_path=Path(".")
        )

    if not os.path.isfile(DBF.pp_objects_dbf_file_path):
        DBF = None

    DUMMY = DummyDatabaseConfiguration()

    ONLINE = \
        OnlineDatabaseConfiguration(
            download_dir_path=Path(__file__).parent.parent.parent / "devdata" / "tcmuseum",
            collection_name='Test'
        )

    if not os.path.isdir(ONLINE.download_dir_path):
        ONLINE = None
