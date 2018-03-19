class Object(object):
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
        pass

    @property
    def name(self):
        raise NotImplementedError

    @property
    def othername(self):
        raise NotImplementedError
