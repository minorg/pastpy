class SitePaginatorPage(object):
    def __init__(self, *, number_one_based, objects, pagination):
        self.__number_one_based = number_one_based
        self.__objects = objects
        self.__pagination = pagination

    @property
    def number_one_based(self):
        return self.__number_one_based

    @property
    def objects(self):
        return self.__objects

    @property
    def pagination(self):
        return self.__pagination