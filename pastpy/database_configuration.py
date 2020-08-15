from typing import NamedTuple, Optional

from pastpy.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class DatabaseConfiguration(NamedTuple):
    dbf: Optional[DbfDatabaseConfiguration] = None
    dummy: Optional[DummyDatabaseConfiguration] = None
    online: Optional[OnlineDatabaseConfiguration] = None
