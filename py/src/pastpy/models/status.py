class Status(object):
    OK = None

    def __init__(self, name, value):
        object.__init__(self)
        self.__name = name
        self.__value = value

    def __int__(self):
        return self.__value

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

    @classmethod
    def value_of(cls, name):
        if name == 'OK' or name == '0':
            return getattr(Status, 'OK')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (Status.OK,)

Status.OK = Status('OK', 0)
