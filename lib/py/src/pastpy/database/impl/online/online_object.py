from pastpy.database.object import Object


class OnlineObject(Object):
    def __init__(self, detail):
        self.__detail = detail

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
        return self.__detail.related_photos

    @property
    def name(self):
        return self.__detail.attributes.get("Object Name")

    @property
    def othername(self):
        return self.__detail.attributes.get("Other Name")
