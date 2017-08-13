class Condition(object):
    EXCELLENT = None
    FAIR = None
    GOOD = None
    NOT_RATED = None
    POOR = None
    UNSTABLE = None

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
        if name == 'EXCELLENT' or name == '0':
            return getattr(Condition, 'EXCELLENT')
        elif name == 'FAIR' or name == '1':
            return getattr(Condition, 'FAIR')
        elif name == 'GOOD' or name == '2':
            return getattr(Condition, 'GOOD')
        elif name == 'NOT_RATED' or name == '3':
            return getattr(Condition, 'NOT_RATED')
        elif name == 'POOR' or name == '4':
            return getattr(Condition, 'POOR')
        elif name == 'UNSTABLE' or name == '5':
            return getattr(Condition, 'UNSTABLE')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (Condition.EXCELLENT, Condition.FAIR, Condition.GOOD, Condition.NOT_RATED, Condition.POOR, Condition.UNSTABLE,)

Condition.EXCELLENT = Condition('EXCELLENT', 0)
Condition.FAIR = Condition('FAIR', 1)
Condition.GOOD = Condition('GOOD', 2)
Condition.NOT_RATED = Condition('NOT_RATED', 3)
Condition.POOR = Condition('POOR', 4)
Condition.UNSTABLE = Condition('UNSTABLE', 5)
