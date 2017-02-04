from pastpy.lib._dbf_table import _DbfTable
from pastpy.lib.models.object_record import ObjectRecord


class ObjectDbfTable(_DbfTable):
    def _map_record(self, record):
        object_record_builder = ObjectRecord.Builder()
        for field_name in self.field_names:
            self._map_record_field(
                field_name=field_name,
                field_value=record[field_name],
                struct_builder=object_record_builder,
                struct_type=ObjectRecord
            )
        return object_record_builder.build()
