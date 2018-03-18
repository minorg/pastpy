from pastpy.object import Object


class DbfObject(Object):
    def __init__(self, record):
        self.__record = record

    @property
    def date(self):
        return self.__record.date

    @property
    def description(self):
        return self.__record.descrip

    @property
    def id(self):
        return self.__record.objectid

    @property
    def name(self):
        return self.__record.name

    @property
    def othername(self):
        return self.__record.othername
