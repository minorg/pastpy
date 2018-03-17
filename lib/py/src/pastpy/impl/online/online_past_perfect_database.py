import os.path
from time import sleep
import http.client


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
            while True:
                page_url_path = webobject_url_path + "?page=" + page_i
                http_client_connection.request("GET", page_url_path)
                response = http_client_connection.getresponse()
                page_contents = response.read()
                if "No results found" in page_contents:
                    break
                page_file_path = os.path.join(pages_dir_path, str(page_i))
                with open(page_file_path, "w+b") as page_file:
                    page_file.write(page_contents.encode())
                sleep(1)
        finally:
            http_client_connection.close()
