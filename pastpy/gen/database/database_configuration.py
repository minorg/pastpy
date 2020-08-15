from typing import NamedTuple, Optional

from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.gen.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.gen.database.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class DatabaseConfiguration(NamedTuple):
    dbf: Optional[DbfDatabaseConfiguration] = None
    dummy: Optional[DummyDatabaseConfiguration] = None
    online: Optional[OnlineDatabaseConfiguration] = None
