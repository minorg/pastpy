from pastpy.database.object import Object
from pastpy.database.impl.online.online_image import OnlineImage


class OnlineObject(Object):
    def __init__(self, *, detail, list_item):
        self.__detail = detail
        self.__list_item = list_item

    @property
    def attributes(self):
        return self.__detail.attributes

    @property
    def date(self):
        return self.__detail.attributes.get("Date")

    @property
    def description(self):
        return self.__detail.attributes.get("Description")

    @property
    def id(self):
        return self.__detail.id

    @property
    def images(self):
        images = []
        if self.__list_item.thumbnail_url:
            images.append(OnlineImage(list_item=self.__list_item))
        if self.__detail.related_photos:
            for detail_image in self.__detail.related_photos:
                images.append(OnlineImage(detail_image=detail_image))
        return tuple(images)

    @property
    def name(self):
        return self.__detail.attributes.get("Object Name")

    @property
    def othername(self):
        return self.__detail.attributes.get("Other Name")

    @property
    def title(self):
        return self.__detail.attributes.get("Title")
