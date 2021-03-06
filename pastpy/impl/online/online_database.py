from typing import Optional

from tqdm import tqdm

from pastpy.database import Database
from pastpy.impl.online.online_file_downloader import OnlineFileDownloader
from pastpy.impl.online.online_file_paths import OnlineFilePaths
from pastpy.impl.online.online_database_object import OnlineDatabaseObject
from pastpy.impl.online.online_database_object_detail_html_parser import (
    OnlineDatabaseObjectDetailHtmlParser,
)
from pastpy.impl.online.online_database_objects_list_html_parser import (
    OnlineDatabaseObjectsListHtmlParser,
)
from pastpy.impl.online.online_database_configuration import OnlineDatabaseConfiguration


class OnlineDatabase(Database):
    def __init__(self, *, configuration: OnlineDatabaseConfiguration):
        Database.__init__(self)

        if configuration.download_dir_path is None:
            configuration = configuration._replace(
                download_dir_path=configuration.collection_name
            )
        self.__configuration = configuration
        self.__file_paths = OnlineFilePaths(configuration.download_dir_path)

    def download(self, tqdm_disable: Optional[bool] = True):
        """
        Download the objects list and object details from PastPerfect Online.
        :param progress_meter_factory: factory method that takes an iterable and returns a new iterable that reports progress
        """

        with OnlineFileDownloader(
            file_paths=self.__file_paths,
            host=self.__configuration.collection_name + ".pastperfectonline.com",
            tqdm_disable=tqdm_disable,
        ) as downloader:
            downloader.download_objects_list()
            objects_list = self.parse_objects_list()
            for objects_list_item in tqdm(
                objects_list, desc="Object details", disable=tqdm_disable
            ):
                guid = self.__object_guid(objects_list_item)
                downloader.download_object_detail(guid=guid)

    def objects(self):
        for objects_list_item in self.parse_objects_list():
            guid = self.__object_guid(objects_list_item)
            try:
                object_detail = self.__parse_object_detail(guid=guid)
            except FileNotFoundError:
                self._logger.debug("object detail for " + guid + " not found")
            yield OnlineDatabaseObject(
                detail=object_detail, list_item=objects_list_item
            )

    def __object_guid(self, objects_list_item):
        return objects_list_item.detail_href.split("/")[-1]

    def __parse_object_detail(self, guid):
        object_detail_file_path = self.__file_paths.object_detail_file_path(guid=guid)
        with open(object_detail_file_path, "rb") as object_detail_file:
            return OnlineDatabaseObjectDetailHtmlParser().parse(
                guid=guid, html=str(object_detail_file.read())
            )

    def parse_object_details(self):
        for objects_list_item in self.parse_objects_list():
            guid = self.__object_guid(objects_list_item)
            try:
                yield self.__parse_object_detail(guid=guid)
            except FileNotFoundError:
                self._logger.debug("object detail for " + guid + " not found")

    def parse_objects_list(self):
        objects_list_page_i = 1
        while True:
            objects_list_page_file_path = self.__file_paths.objects_list_page_file_path(
                objects_list_page_i
            )
            if not objects_list_page_file_path.is_file():
                return
            with open(objects_list_page_file_path, "rb") as objects_list_page_file:
                objects_list_page_html = str(objects_list_page_file.read())

            objects_list_html_parser = OnlineDatabaseObjectsListHtmlParser()
            for objects_list_item in objects_list_html_parser.parse(
                objects_list_page_html
            ):
                yield objects_list_item

            objects_list_page_i = objects_list_page_i + 1
