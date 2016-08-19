class _DbfTable(object):
    def __init__(self, table):
        self.__table = table

    def _map_record(self, record):
        raise NotImplementedError

    def __enter__(self):
        pass

    def __exit__(self):
        self.__table.close()

    @property
    def field_names(self):
        return self.__table.field_names

    @classmethod
    def open(cls, dbf_file_path):
        if dbf_file_path.endswith('.dbf'):
            dbf_file_path = dbf_file_path[:-len('.dbf')]

        import dbf
        table = dbf.Table(dbf_file_path)
        table.open()
        return cls(table)

    def records(self):
        for record in self.__table:
            yield self._map_record(record)
        raise StopIteration

    def thrift_field_names(self):
        for field_name in self.field_names:
            yield "    // @validation {\"minLength\": 1}\n    optional string %s;\n" % field_name
