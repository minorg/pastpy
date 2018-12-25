from pastpy.database.database_object import DatabaseObject


class DummyDatabaseObject(DatabaseObject):
    def __init__(self, *, configuration, index):
        self.__configuration = configuration
        self.__date = date.now()
        self.__index = index

    @property
    def date(self):
