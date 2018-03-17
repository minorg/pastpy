class Object(object):
    @property
    def description(self):
        raise NotImplementedError

    @property
    def id(self):
        raise NotImplementedError
