from pastpy.database.image import Image
from pastpy.gen.database.impl.online.online_object_detail_image import OnlineObjectDetailImage
from pastpy.gen.database.impl.online.online_objects_list_item import OnlineObjectsListItem


class OnlineImage(Image):
    def __init__(self, *, detail_image=None, list_item=None):
        assert (detail_image is not None) ^ (list_item is not None)
        self.__detail_image = detail_image
        assert detail_image is None or isinstance(detail_image, OnlineObjectDetailImage)
        self.__list_item = list_item
        assert list_item is None or isinstance(list_item, OnlineObjectsListItem)

    @property
    def full_size_url(self):
        if self.__detail_image is not None:
            return self.__detail_image.full_size_url
        else:
            return None

    def __getattr__(self, attr):
        return getattr(self.__detail_image, attr)

    @property
    def thumbnail_url(self):
        if self.__detail_image is not None:
            return self.__detail_image.thumbnail_url
        else:
            return self.__list_item.thumbnail_url

    @property
    def title(self):
        if self.__detail_image is not None:
            return self.__detail_image.title
        else:
            return self.__list_item.title
