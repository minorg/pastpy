from pastpy._dbf_table import _DbfTable


class ObjectDbfTable(_DbfTable):
    def _map_record(self, record):
        return record
