class Object(object):
    @property
    def attributes(self):
        raise NotImplementedError

    @property
    def date(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError

    @property
    def id(self):
        raise NotImplementedError

    @property
    def images(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def othername(self):
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError
