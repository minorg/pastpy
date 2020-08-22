from abc import ABC, abstractmethod
from pastpy.database_image import DatabaseImage
from typing import Dict, Iterable, Union


class DatabaseObject(ABC):
    @property
    @abstractmethod
    def date(self) -> Union[object, None]:
        """
        @return date of the object
        """

    @property
    @abstractmethod
    def description(self) -> Union[str, None]:
        """
        @return description of the object
        """

    @property
    @abstractmethod
    def id(self) -> str:
        """
        @return id of the object
        """

    @property
    @abstractmethod
    def impl_attributes(self) -> Dict[str, object]:
        """
        @return dict of implementation-defined attributes where neither keys nor values is None
        """

    @property
    @abstractmethod
    def images(self) -> Iterable[DatabaseImage]:
        """
        @return iterable of DatabaseImage instances
        """

    @property
    @abstractmethod
    def name(self) -> Union[str, None]:
        """
        @return name of object
        """

    @property
    @abstractmethod
    def othername(self) -> Union[str, None]:
        """
        @return alternative name of object
        """

    @property
    @abstractmethod
    def title(self) -> Union[str, None]:
        """
        @return title of object
        """
