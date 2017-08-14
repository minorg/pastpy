class CardinalDirection(object):
    E = None
    N = None
    S = None
    W = None

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
        if name == 'E' or name == '0':
            return getattr(CardinalDirection, 'E')
        elif name == 'N' or name == '1':
            return getattr(CardinalDirection, 'N')
        elif name == 'S' or name == '2':
            return getattr(CardinalDirection, 'S')
        elif name == 'W' or name == '3':
            return getattr(CardinalDirection, 'W')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (CardinalDirection.E, CardinalDirection.N, CardinalDirection.S, CardinalDirection.W,)

CardinalDirection.E = CardinalDirection('E', 0)
CardinalDirection.N = CardinalDirection('N', 1)
CardinalDirection.S = CardinalDirection('S', 2)
CardinalDirection.W = CardinalDirection('W', 3)
