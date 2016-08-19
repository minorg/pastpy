from pastpy._dbf_table import _DbfTable
from pastpy.models.object import Object


class ObjectDbfTable(_DbfTable):
    def _map_record(self, record):
        object_builder = Object.Builder()
        for field_name in self.field_names:
            field_metadata = getattr(Object.FieldMetadata, field_name.upper())
            field_value = \
                self._map_record_field(
                    field_metadata=field_metadata,
                    field_name=field_name,
                    field_value=record[field_name]
                )

            if field_value is None:
                continue

            try:
                getattr(object_builder, 'set_' + field_name)(field_value)
            except TypeError, e:
                raise TypeError("%(field_value)s: %(e)s" % locals())
            except ValueError, e:
                if field_metadata.validation is not None:
                    continue
                raise ValueError("%(field_value)s: %(e)s" % locals())

        return object_builder.build()
