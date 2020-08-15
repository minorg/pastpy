from typing import NamedTuple


class DummyDatabaseConfiguration(NamedTuple):
    images_per_object: int = 2
    objects: int = 2
