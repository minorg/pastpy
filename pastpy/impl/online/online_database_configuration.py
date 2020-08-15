from pathlib import Path
from typing import NamedTuple, Optional


class OnlineDatabaseConfiguration(NamedTuple):
    collection_name: str
    download_dir_path: Optional[Path] = None
