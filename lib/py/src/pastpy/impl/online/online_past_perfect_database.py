import os.path
from pastpy.impl.online.downloader import Downloader
from pastpy.impl.online.file_paths import FilePaths


class OnlinePastPerfectDatabase(object):
    # class _Parser(object):
    #     def parse_objects_list_page(self, html):
    #         class HtmlParser(html.parser.HTMLParser):
    #             def handle_starttag(self, tag, attrs):
    #                 print("Encountered a start tag:", tag)

    #             def handle_endtag(self, tag):
    #                 print("Encountered an end tag :", tag)

    #             def handle_data(self, data):
    #                 print("Encountered some data  :", data)

    #         pass

    def __init__(self, *, collection_name, download_dir_path=None):
        self.__collection_name = collection_name
        if download_dir_path is None:
            download_dir_path = collection_name
        self.__file_paths = FilePaths(download_dir_path)

    def download(self):
        with Downloader(file_paths=self.__file_paths, host=self.__collection_name + ".pastperfectonline.com") as downloader:
            downloader.download_objects_list()

            page_i = 1
            while True:
                page_file_path = self.__file_paths.objects_list_page_file_path(page_i)
                if not os.path.isfile(page_file_path):
                    break
