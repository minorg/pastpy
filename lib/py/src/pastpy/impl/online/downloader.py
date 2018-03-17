import http.client
import logging
import os.path
from time import sleep


class Downloader(object):
    def __init__(self, *, file_paths, host):
        self.__http_client_connection = None
        self.__file_paths = file_paths
        self.__host = host

    def download_object_detail(self, *, guid):
        pass

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
            logging.debug("page file %s already exists, skipping", page_file_path)
            page_i = page_i + 1
            return True
        page_url_path = "/webobject?page=" + str(page_i)
        logging.debug("retrieving %s", page_url_path)
        self.__http_client_connection.request("GET", page_url_path)
        response = self.__http_client_connection.getresponse()
        page_contents = response.read()
        logging.debug("retrieved %s", page_url_path)
        if "No results found" in str(page_contents):
            logging.debug("page %d was the last, stopping", page_i)
            return False
        with open(page_file_path, "w+b") as page_file:
            page_file.write(page_contents)
            logging.info("wrote %s", page_file_path)
        sleep(1)
        return True

    def __enter__(self):
        if not os.path.isdir(self.__file_paths.root_dir_path):
            os.makedirs(self.__file_paths.root_dir_path)

        self.__http_client_connection = http.client.HTTPConnection(self.__host)

        return self

    def __exit__(self, *args, **kwds):
        self.__http_client_connection.close()
