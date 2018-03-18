class OnlineImageType(object):
    INDIVIDUAL = None
    LARGE = None

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
        if name == 'INDIVIDUAL' or name == '0':
            return getattr(OnlineImageType, 'INDIVIDUAL')
        elif name == 'LARGE' or name == '1':
            return getattr(OnlineImageType, 'LARGE')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (OnlineImageType.INDIVIDUAL, OnlineImageType.LARGE,)

OnlineImageType.INDIVIDUAL = OnlineImageType('INDIVIDUAL', 0)
OnlineImageType.LARGE = OnlineImageType('LARGE', 1)
