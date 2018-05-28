from abc import ABC, abstractproperty


class DatabaseObject(ABC):
    @abstractproperty
    def date(self):
        pass

    @abstractproperty
    def description(self):
        pass

    @abstractproperty
    def id(self):
        pass

    @abstractproperty
    def impl_attributes(self):
        pass

    @abstractproperty
    def images(self):
        pass

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def othername(self):
        pass

    @abstractproperty
    def title(self):
        pass
