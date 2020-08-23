from abc import ABC, abstractmethod
from typing import Dict, Iterable, Optional

from pastpy.database_image import DatabaseImage


class DatabaseObject(ABC):
    @property
    @abstractmethod
    def date(self) -> Optional[object]:
        """
        @return date of the object
        """

    @property
    @abstractmethod
    def description(self) -> Optional[str]:
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
    def name(self) -> Optional[str]:
        """
        @return name of object
        """

    @property
    @abstractmethod
    def othername(self) -> Optional[str]:
        """
        @return alternative name of object
        """

    @property
    @abstractmethod
    def title(self) -> Optional[str]:
        """
        @return title of object
        """
