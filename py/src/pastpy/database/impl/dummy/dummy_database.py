from pastpy.database.database import Database
from pastpy.gen.database.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration


class DummyDatabase(Database):
    def __init__(self, *, configuration):
        Database.__init__(self)
        assert isinstance(configuration, DummyDatabaseConfiguration)
