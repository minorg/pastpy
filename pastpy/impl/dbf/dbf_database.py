from pastpy.database import Database
from pastpy.impl.dbf.objects_dbf_table import ObjectsDbfTable
from pastpy.impl.dbf.dbf_database_object import DbfDatabaseObject
from pastpy.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration


class DbfDatabase(Database):
    def __init__(self, *, configuration: DbfDatabaseConfiguration):
        Database.__init__(self)

        if (
            configuration.pp_images_dir_path is not None
            and configuration.pp_objects_dbf_file_path is not None
        ):
            self.__configuration = configuration
            return

        pp_install_dir_path = configuration.pp_install_dir_path
        if pp_install_dir_path is None:
            pp_install_dir_path = "C:\\pp5"

        if not pp_install_dir_path.is_dir():
            raise ValueError(
                "PastPerfect installation directory %s does not exist"
                % pp_install_dir_path
            )
        if configuration.pp_images_dir_path is None:
            configuration = configuration._replace(
                pp_images_dir_path=pp_install_dir_path / "Images"
            )
        if configuration.pp_objects_dbf_file_path is None:
            configuration = configuration._replace(
                pp_objects_dbf_file_path=pp_install_dir_path / "Data" / "OBJECTS.DBF"
            )

        if not configuration.pp_images_dir_path.is_dir():
            raise ValueError(
                "PastPerfect images directory %s does not exist"
                % configuration.pp_images_dir_path
            )
        if not configuration.pp_objects_dbf_file_path.is_file():
            raise ValueError(
                "PastPerfect objects DBF file %s does not exist"
                % configuration.pp_objects_dbf_file_path
            )

        self.__configuration = configuration

    def objects(self):
        with ObjectsDbfTable.open(
            self.__configuration.pp_objects_dbf_file_path
        ) as table:
            for record in table.records():
                yield DbfDatabaseObject(
                    images_dir_path=self.__configuration.pp_images_dir_path,
                    record=record,
                )
