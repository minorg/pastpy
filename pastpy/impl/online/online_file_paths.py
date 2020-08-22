from pathlib import Path


class OnlineFilePaths:
    def __init__(self, root_dir_path: Path):
        assert root_dir_path is not None
        self.__root_dir_path = root_dir_path

    def object_detail_file_path(self, guid: str) -> Path:
        return self.object_details_dir_path / (guid + ".html")

    @property
    def object_details_dir_path(self) -> Path:
        return self.__root_dir_path / "objects" / "detail"

    @property
    def objects_list_dir_path(self) -> Path:
        return self.__root_dir_path / "objects" / "list"

    def objects_list_page_file_path(self, page_i) -> Path:
        return self.objects_list_dir_path / (str(page_i) + ".html")

    @property
    def root_dir_path(self) -> Path:
        return self.__root_dir_path
