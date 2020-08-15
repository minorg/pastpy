from typing import Dict, Tuple, NamedTuple

from pastpy.gen.database.impl.online.online_database_object_detail_image import OnlineDatabaseObjectDetailImage


class OnlineDatabaseObjectDetail(NamedTuple):
    attributes: Dict[str, str]
    guid: str
    id: str
    related_photos: Tuple[OnlineDatabaseObjectDetailImage, ...]
