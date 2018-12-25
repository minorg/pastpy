from pastpy.database.database_object import DatabaseObject
import datetime


class DummyDatabaseObject(DatabaseObject):
    def __init__(self, *, configuration, index):
        self.__configuration = configuration
        self.__date = datetime.date.today().isoformat()
        self.__index = index

    @property
    def date(self):
        assert False
        return self.__date
