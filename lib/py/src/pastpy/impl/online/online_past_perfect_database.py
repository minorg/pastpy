import os.path
from time import sleep
import http.client
import logging


class OnlinePastPerfectDatabase(object):
    def __init__(self, name, dir_path=None):
        self.__name = name
        if dir_path is None:
            dir_path = os.path.abspath(self.__name)
        self.__dir_path = dir_path

    def download(self):
        if not os.path.isdir(self.__dir_path):
            os.makedirs(self.__dir_path)
        http_client_connection = http.client.HTTPConnection(self.__name + ".pastperfectonline.com")
        try:
            webobject_url_path = "/webobject"
            page_i = 1
            pages_dir_path = os.path.join(self.__dir_path, "objects", "list")
            if not os.path.isdir(pages_dir_path):
                os.makedirs(pages_dir_path)
                logging.info("created directory %s", pages_dir_path)
            while True:
                page_file_path = os.path.join(pages_dir_path, str(page_i) + ".html")
                if os.path.isfile(page_file_path):
                    logging.info("page file %s already exists, skipping", page_file_path)
                    page_i = page_i + 1
                    continue
                page_url_path = webobject_url_path + "?page=" + str(page_i)
                logging.info("retrieving %s", page_url_path)
                http_client_connection.request("GET", page_url_path)
                response = http_client_connection.getresponse()
                page_contents = response.read()
                logging.info("retrieved %s", page_url_path)
                if "No results found" in str(page_contents):
                    logging.info("page %d was the last, stopping", page_i)
                    break
                with open(page_file_path, "w+b") as page_file:
                    page_file.write(page_contents)
                    logging.info("wrote %s", page_file_path)
                sleep(1)
                page_i = page_i + 1
                # break
        finally:
            http_client_connection.close()
