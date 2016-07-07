class _DbfTable(object):
    def __init__(self, table):
        self.__table = table
        for field_name in table.field_names:
            print "    // @validation {\"minLength\": 1}\n    optional string %s;\n" % field_name

    def _map_record(self, record):
        raise NotImplementedError

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
