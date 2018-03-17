import os.path
from pastpy.impl.online.downloader import Downloader
from pastpy.impl.online.file_paths import FilePaths
from pastpy.impl.online.objects_list_html_parser import ObjectsListHtmlParser


class OnlinePastPerfectDatabase(object):
    def __init__(self, *, collection_name, download_dir_path=None):
        self.__collection_name = collection_name
        if download_dir_path is None:
            download_dir_path = collection_name
        self.__file_paths = FilePaths(download_dir_path)

    def download(self):
        # with Downloader(file_paths=self.__file_paths, host=self.__collection_name + ".pastperfectonline.com") as downloader:
        #     downloader.download_objects_list()
        self.__parse_objects_list()

    def parse_objects_list(self):
        objects_list_page_i = 1
        while True:
            objects_list_page_file_path = self.__file_paths.objects_list_page_file_path(objects_list_page_i)
            if not os.path.isfile(objects_list_page_file_path):
                break
            with open(objects_list_page_file_path, "rb") as objects_list_page_file:
                objects_list_page_html = str(objects_list_page_file.read())

            objects_list_html_parser = ObjectsListHtmlParser()
            objects_list_html_parser.feed(objects_list_page_html)

            objects_list_page_i = objects_list_page_i + 1
