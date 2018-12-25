from pastpy.database.database_image import DatabaseImage


class DummyDatabaseImage(DatabaseImage):
    def __init__(self, *, image_index, object_index):
        self.__image_index = image_index
        self.__object_inedx = object_index

