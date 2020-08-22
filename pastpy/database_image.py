from abc import ABC, abstractmethod, abstractproperty
from typing import Union


class DatabaseImage(ABC):
    @property
    @abstractmethod
    def full_size_url(self) -> Union[str, None]:
        """
        @return full size URL of the image
        """

    @property
    @abstractmethod
    def thumbnail_url(self) -> Union[str, None]:
        """
        @return thumbnail URL of the image
        """

    @property
    @abstractmethod
    def title(self) -> Union[str, None]:
        """
        @return title of the image
        """
