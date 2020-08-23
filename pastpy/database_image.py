from abc import ABC, abstractmethod
from typing import Optional


class DatabaseImage(ABC):
    @property
    @abstractmethod
    def full_size_url(self) -> Optional[str]:
        """
        @return full size URL of the image
        """

    @property
    @abstractmethod
    def thumbnail_url(self) -> Optional[str]:
        """
        @return thumbnail URL of the image
        """

    @property
    @abstractmethod
    def title(self) -> Optional[str]:
        """
        @return title of the image
        """
