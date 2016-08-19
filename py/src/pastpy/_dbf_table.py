from datetime import datetime, date
import logging


class _DbfTable(object):
    def __init__(self, table):
        self.__table = table

    def _map_record(self, record):
        raise NotImplementedError

    def _map_record_field(self, field_metadata, field_name, field_value):
        if field_value is None:
            return field_value

        if isinstance(field_value, basestring):
            field_value = field_value.strip()
            if len(field_value) == 0:
                return None

        if field_metadata.type == datetime:
            if isinstance(field_value, date):
                field_value = datetime(year=field_value.year, month=field_value.month, day=field_value.day)
            elif isinstance(field_value, datetime):
                pass
            elif isinstance(field_value, basestring):
                logging.warn("unable to parse %(field_name)s=%(field_value)s (basestring)" % locals())
                return None
            elif isinstance(field_value, int):
                if field_value == 0:
                    return None
                raise NotImplementedError("%(field_name)s: %(field_value)s" % locals())
        elif field_metadata.type == object:
            pass
        elif field_metadata.type == str:
            if not isinstance(field_value, basestring):
                logging.info("converting %s=%s (%s) to string", field_name, field_value, type(field_value))
                field_value = str(field_value)
        else:
            if hasattr(field_metadata.type, 'value_of'):
                try:
                    field_value = field_metadata.type.value_of(str(field_value).upper().replace(' ', '_'))
                except ValueError, e:
                    field_value_type = type(field_value)
                    field_metadata_type = field_metadata.type
                    logging.warn("unable to convert %(field_name)s=%(field_value)s (%(field_value_type)s) to %(field_metadata_type)s: %(e)s" % locals())
                    return None
            else:
                try:
                    field_value = field_metadata.type(field_value)
                except (TypeError, ValueError), e:
                    raise TypeError("unable to coerce %s=%s (%s) to a %s: %s" % (field_name, field_value, type(field_value), field_metadata.type, e))
        return field_value

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
