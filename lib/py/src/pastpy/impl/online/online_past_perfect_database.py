import os.path
from time import sleep
import http.client
import logging


class OnlinePastPerfectDatabase(object):
    class _Downloader(object):
        def __init__(self, *, file_paths, host):
            self.__http_client_connection = None
            self.__file_paths = file_paths
            self.__host = host

        def download_objects_list(self):
            objects_list_dir_path = self.__file_paths.objects_list_dir_path
            if not os.path.isdir(objects_list_dir_path):
                os.makedirs(objects_list_dir_path)
                logging.info("created directory %s", objects_list_dir_path)

            page_i = 1
            while self.__download_objects_list_page(page_i):
                page_i = page_i + 1

        def __download_objects_list_page(self, page_i):
            page_file_path = self.__file_paths.objects_list_page_file_path(page_i)
            if os.path.isfile(page_file_path):
                logging.info("page file %s already exists, skipping", page_file_path)
                page_i = page_i + 1
                return True
            page_url_path = "/webobject?page=" + str(page_i)
            logging.info("retrieving %s", page_url_path)
            self.__http_client_connection.request("GET", page_url_path)
            response = self.__http_client_connection.getresponse()
            page_contents = response.read()
            logging.info("retrieved %s", page_url_path)
            if "No results found" in str(page_contents):
                logging.info("page %d was the last, stopping", page_i)
                return False
            with open(page_file_path, "w+b") as page_file:
                page_file.write(page_contents)
                logging.info("wrote %s", page_file_path)
            return True

        def __enter__(self):
            if not os.path.isdir(self.__file_paths.root_dir_path):
                os.makedirs(self.__file_paths.root_dir_path)

            self.__http_client_connection = http.client.HTTPConnection(self.__host)

            return self

        def __exit__(self, *args, **kwds):
            self.__http_client_connection.close()

    class _FilePaths(object):
        def __init__(self, root_dir_path):
            self.__root_dir_path = root_dir_path

        @property
        def objects_list_dir_path(self):
            return os.path.join(self.__root_dir_path, "objects", "list")

        def objects_list_page_file_path(self, page_i):
            return os.path.join(self.objects_list_dir_path, str(page_i) + ".html")

        @property
        def root_dir_path(self):
            return self.__root_dir_path

    def __init__(self, *, name, dir_path=None):
        self.__name = name
        if dir_path is None:
            dir_path = os.path.abspath(self.__name)
        self.__file_paths = OnlinePastPerfectDatabase._FilePaths(dir_path)

    def download(self):
        with OnlinePastPerfectDatabase._Downloader(file_paths=self.__file_paths, host=self.__name + ".pastperfectonline.com") as downloader:
            downloader.download_objects_list()
