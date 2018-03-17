import os.path


class FilePaths(object):
    def __init__(self, root_dir_path):
        assert root_dir_path is not None
        self.__root_dir_path = root_dir_path

    @property
    def objects_list_dir_path(self):
        return os.path.join(self.__root_dir_path, "objects", "list")

    def objects_list_page_file_path(self, page_i):
        return os.path.join(self.objects_list_dir_path, str(page_i) + ".html")

    @property
    def root_dir_path(self):
        return self.__root_dir_path
