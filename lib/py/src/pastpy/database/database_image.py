from abc import ABC, abstractproperty


class DatabaseImage(ABC):
    @abstractproperty
    def full_size_url(self):
        pass

    @abstractproperty
    def thumbnail_url(self):
        pass

    @abstractproperty
    def title(self):
        pass
