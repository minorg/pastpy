from typing import NamedTuple, Optional

from pastpy.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class DatabaseConfiguration(NamedTuple):
    dbf: Optional[DbfDatabaseConfiguration] = None
    dummy: Optional[DummyDatabaseConfiguration] = None
    online: Optional[OnlineDatabaseConfiguration] = None
