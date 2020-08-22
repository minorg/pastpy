from abc import abstractmethod
import logging
from pastpy.database_object import DatabaseObject
from pastpy.impl.dbf.dbf_database_configuration import DbfDatabaseConfiguration
from pastpy.impl.dummy.dummy_database_configuration import DummyDatabaseConfiguration
from pastpy.impl.online.online_database_configuration import OnlineDatabaseConfiguration
from typing import Iterable, Union


class Database:
    def __init__(self):
        self._logger = logging.getLogger(self.__class__.__name__)

    @classmethod
    def create(
        cls,
        configuration: Union[
            DbfDatabaseConfiguration,
            DummyDatabaseConfiguration,
            OnlineDatabaseConfiguration,
        ],
    ):
        if isinstance(configuration, DbfDatabaseConfiguration):
            from pastpy.impl.dbf.dbf_database import DbfDatabase

            return DbfDatabase(configuration=configuration)
        elif isinstance(configuration, DummyDatabaseConfiguration):
            from pastpy.impl.dummy.dummy_database import DummyDatabase

            return DummyDatabase(configuration=configuration)
        elif isinstance(configuration, OnlineDatabaseConfiguration):
            from pastpy.impl.online.online_database import OnlineDatabase

            return OnlineDatabase(configuration=configuration)
        else:
            raise NotImplementedError

    @abstractmethod
    def objects(self) -> Iterable[DatabaseObject]:
        """
        Iterate over the objects in the database.
        @return an iterable of objects
        """
        pass
