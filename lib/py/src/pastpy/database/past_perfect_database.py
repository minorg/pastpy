class PastPerfectDatabase(object):
    @classmethod
    def create_from_dbf(cls, *, pp_images_dir_path=None, pp_install_dir_path=None, pp_objects_dbf_file_path=None):
        from pastpy.database.impl.dbf.dbf_past_perfect_database import DbfPastPerfectDatabase
        return DbfPastPerfectDatabase(pp_images_dir_path=pp_images_dir_path, pp_install_dir_path=pp_install_dir_path, pp_objects_dbf_file_path=pp_objects_dbf_file_path)

    @classmethod
    def create_from_online(cls, *, collection_name, download_dir_path=None):
        from pastpy.database.impl.online.online_past_perfect_database import OnlinePastPerfectDatabase
        return OnlinePastPerfectDatabase(collection_name=collection_name, download_dir_path=download_dir_path)

    def objects(self):
        """
        Iterate over the objects in the database.
        @return an iterable of objects
        """
        raise NotImplementedError
