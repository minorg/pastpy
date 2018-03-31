import os.path
from pastpy.database.database import Database
from pastpy.database.impl.dbf.objects_dbf_table import ObjectsDbfTable
from pastpy.database.impl.dbf.dbf_database_object import DbfDatabaseObject
from pastpy.gen.database.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration


class DbfDatabase(Database):
    def __init__(self, *, configuration):
        Database.__init__(self)
        assert isinstance(configuration, DbfDatabaseConfiguration)
        configuration_builder = configuration.replacer()
        if configuration.download_dir_path is None:
            configuration_builder.download_dir_path = configuration.collection_name
        configuration = configuration_builder.build()
        if configuration.pp_install_dir_path is not None:
            if not os.path.isdir(configuration.pp_install_dir_path):
                raise ValueError(
                    "PastPerfect installation directory %s does not exist" % configuration.pp_install_dir_path)
            if configuration.pp_images_dir_path is None:
                configuration_builder.pp_images_dir_path = os.path.join(
                    configuration.pp_install_dir_path, 'Images')
            if configuration.pp_objects_dbf_file_path is None:
                configuration_builder.pp_objects_dbf_file_path = os.path.join(
                    configuration.pp_install_dir_path, 'Data', 'OBJECTS.DBF')
        elif configuration.pp_images_dir_path is None:
            raise ValueError(
                "must specify a PastPerfect installation directory or an images directory")
        elif configuration.pp_objects_dbf_file_path is None:
            raise ValueError(
                "must specify a PastPerfect installation directory or an objects DBF file")
        configuration = configuration_builder.build()

    def objects(self):
        with ObjectsDbfTable.open(self.__configuration.pp_objects_dbf_file_path) as table:
            for record in table.records():
                yield DbfDatabaseObject(images_dir_path=self.__configuration.pp_images_dir_path, record=record)
