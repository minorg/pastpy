from typing import NamedTuple, Optional


class OnlineDatabaseObjectsListItem(NamedTuple):
    detail_href: str
    record_type: str
    title: str
    thumbnail_url: Optional[str] = None
