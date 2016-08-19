from datetime import datetime

from pastpy._dbf_table import _DbfTable
from pastpy.models.object import Object


class ObjectDbfTable(_DbfTable):
    def _map_record(self, record):
        object_builder = Object.Builder()
        for field_name in self.field_names:
            field_metadata = getattr(Object.FieldMetadata, field_name.upper())
            field_value = record[field_name]

            if field_value is None:
                continue
            elif isinstance(field_value, basestring):
                if len(field_value) == 0:
                    continue

            if field_metadata.type == str:
                pass
            elif field_metadata.type == datetime:
                if isinstance(field_value, basestring):
                    field_value = field_value.strip()
                    if len(field_value) == 0:
                        continue
                if isinstance(field_value, int):
                    if field_value == 0:
                        continue
                raise NotImplementedError("%(field_name)s: %(field_value)s" % locals())
            else:
                if isinstance(field_value, basestring):
                    field_value = field_value.strip()
                    if len(field_value) == 0:
                        continue
                if hasattr(field_metadata.type, 'value_of'):
                    field_value = field_metadata.type.value_of(field_value.upper())
                else:
                    try:
                        field_value = field_metadata.type(field_value)
                    except (TypeError, ValueError), e:
                        raise TypeError("unable to coerce %s (%s) to a %s: %s" % (field_value, type(field_value), field_metadata.type, e))

            try:
                getattr(object_builder, 'set_' + field_name)(field_value)
            except TypeError, e:
                raise TypeError("%(field_value)s: %(e)s" % locals())
            except ValueError, e:
                raise TypeError("%(field_value)s: %(e)s" % locals())

        return object_builder.build()
