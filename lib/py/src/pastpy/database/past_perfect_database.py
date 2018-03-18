class PastPerfectDatabase(object):
    @classmethod
    def create_from_dbf(cls, data_dir_path):
        from pastpy.database.impl.dbf.dbf_past_perfect_database import DbfPastPerfectDatabase
        return DbfPastPerfectDatabase(data_dir_path=data_dir_path)

    @classmethod
    def create_from_online(cls, collection_name, download_dir_path=None):
        from pastpy.database.impl.online.online_past_perfect_database import OnlinePastPerfectDatabase
        return OnlinePastPerfectDatabase(collection_name=collection_name, download_dir_path=download_dir_path)

    def objects(self):
        """
        Iterate over the objects in the database.
        @return an iterable of objects
        """
        raise NotImplementedError
