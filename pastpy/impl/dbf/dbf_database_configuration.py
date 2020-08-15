from pathlib import Path
from typing import Optional, NamedTuple


class DbfDatabaseConfiguration(NamedTuple):
    pp_images_dir_path: Optional[Path] = None
    pp_install_dir_path: Optional[Path] = None
    pp_objects_dbf_file_path: Optional[Path] = None
