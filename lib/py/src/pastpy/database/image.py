class Image(object):
    @property
    def full_size_url(self):
        raise NotImplementedError

    @property
    def thumbnail_url(self):
        raise NotImplementedError

    @property
    def title(self):
        raise NotImplementedError
