import logging
import os.path


class Database(object):
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

    @classmethod
    def create(cls, database):
        if os.path.isdir(os.path.join(database, "Data")):
            return Database.create_from_dbf(pp_install_dir_path=database)
        else:
            return Database.create_from_online(collection_name=database)

    @classmethod
    def create_from_dbf(cls, *, pp_images_dir_path=None, pp_install_dir_path=None, pp_objects_dbf_file_path=None):
        from pastpy.database.impl.dbf.dbf_database import DbfDatabase
        return DbfDatabase(pp_images_dir_path=pp_images_dir_path, pp_install_dir_path=pp_install_dir_path, pp_objects_dbf_file_path=pp_objects_dbf_file_path)

    @classmethod
    def create_from_online(cls, *, collection_name, download_dir_path=None):
        from pastpy.database.impl.online.online_database import OnlineDatabase
        return OnlineDatabase(collection_name=collection_name, download_dir_path=download_dir_path)

    def objects(self):
        """
        Iterate over the objects in the database.
        @return an iterable of objects
        """
        raise NotImplementedError
