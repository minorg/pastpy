import logging
import os.path
from pastpy.database.object import Object
from pastpy.database.impl.dbf.dbf_image import DbfImage


class DbfObject(Object):
    def __init__(self, *, images_dir_path, record):
        self.__images = None
        self.__images_dir_path = images_dir_path
        self.__logger = logging.getLogger(self.__class__.__name__)
        self.__record = record

    @property
    def date(self):
        return self.__record.date

    @property
    def description(self):
        return self.__record.descrip

    @property
    def id(self):
        return self.__record.objectid

    @property
    def images(self):
        if self.__images is not None:
            return self.__images

        if not self.__record.imageno or self.__record.objectid is None:
            self.__images = tuple()
            return self.__images

        if not os.path.isdir(self.__images_dir_path):
            raise ValueError(
                "PastPerfect images directory %s does not exist" % self.__images_dir_path)

        images = []
        pp_image_i = 0
        while pp_image_i < self.__record.imageno:
            pp_image_file_name = self.__record.objectid
            if pp_image_i > 0:
                pp_image_file_name = pp_image_file_name + \
                    '-' + str(pp_image_i)
            pp_image_i = pp_image_i + 1
            pp_image_file_name = pp_image_file_name + '.jpg'
            pp_image_file_path = os.path.join(
                self.__images_dir_path, pp_image_file_name)
            if not os.path.isfile(pp_image_file_path):
                self.__logger.debug(
                    "object %s image %s does not exist", self.__record.objectid, pp_image_file_path)
                break
            images.append(DbfImage(file_path=pp_image_file_path))
        self.__images = tuple(images)
        return self.__images

    @property
    def name(self):
        return self.__record.name

    @property
    def othername(self):
        return self.__record.othername
