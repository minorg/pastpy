import os.path
from time import sleep
import http.client


class PastPerfectOnline(object):
    def __init__(self, name):
        self.__name = name

    def download(self, dir_path=None):
        if dir_path is None:
            dir_path = os.path.abspath(self.__name)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        http_client_connection = http.client.HTTPConnection(self.__name + ".pastperfectonline.com")
        try:
            webobject_url_path = "/webobject"
            page_i = 1
            pages_dir_path = os.path.join(dir_path, "objects", "list")
            if not os.path.isdir(pages_dir_path):
                os.makedirs(pages_dir_path)
            while True:
                page_url_path = webobject_url_path + "?page=" + page_i
                http_client_connection.request("GET", page_url_path)
                response = http_client_connection.getresponse()
                page_contents = response.read()
                if "No results found" in page_contents:
                    break
                page_file_path = os.path.join(pages_dir_path, "page-" + str(page_i))
                with open(page_file_path, "w+b") as page_file:
                    page_file.write(page_contents.encode())
                sleep(1)
        finally:
            http_client_connection.close()


if __name__ == "__main__":
    from argparse import ArgumentParser
    argument_parser = ArgumentParser()
    argument_parser.add_argument("name", help="name of PastPerfect Online site e.g., yoursite in http://yoursite.pastperfectonline.com")
    argument_parser.add_argument('--download-dir-path', help="path for downloaded files, defaults to ./name")
    args = argument_parser.parse_args()

    PastPerfectOnline(name=args.name).download(dir_path=args.download_dir_path)
