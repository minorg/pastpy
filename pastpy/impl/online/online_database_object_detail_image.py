from typing import NamedTuple

from pastpy.impl.online.online_database_object_detail_image_type import OnlineDatabaseObjectDetailImageType


class OnlineDatabaseObjectDetailImage(NamedTuple):
    full_size_url: str
    mediaid: str
    objectid: str
    src: str
    thumbnail_url: str
    title: str
    type: OnlineDatabaseObjectDetailImageType
