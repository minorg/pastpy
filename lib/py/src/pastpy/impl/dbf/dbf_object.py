from pastpy.object import Object


class DbfObject(Object):
    def __init__(self, record):
        self.__record = record

    def __getattr__(self, attr):
        return getattr(self.__record, attr)
