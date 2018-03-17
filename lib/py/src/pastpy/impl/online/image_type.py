class ImageType(object):
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
            return getattr(ImageType, 'INDIVIDUAL')
        elif name == 'LARGE' or name == '1':
            return getattr(ImageType, 'LARGE')
        raise ValueError(name)

    @classmethod
    def values(cls):
        return (ImageType.INDIVIDUAL, ImageType.LARGE,)

ImageType.INDIVIDUAL = ImageType('INDIVIDUAL', 0)
ImageType.LARGE = ImageType('LARGE', 1)
