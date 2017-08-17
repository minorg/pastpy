from datetime import datetime, date
import logging


class _DbfTable(object):
    def __init__(self, table):
        self.__table = table

    def _coerce_record_field(
        self,
        field_metadata,
        field_value,
        field_number=None,
        existing_field_value=None
    ):
        field_name = field_metadata.name
        if field_metadata.type == datetime:
            if isinstance(field_value, date):
                return datetime(year=field_value.year, month=field_value.month, day=field_value.day)
            elif isinstance(field_value, datetime):
                return field_value
            elif isinstance(field_value, str):
                for strptime_format in ('%m/%d/%Y', '%Y'):
                    try:
                        return datetime.strptime(field_value, strptime_format)
                    except ValueError:
                        pass
                logging.warn("unable to parse %(field_name)s=%(field_value)s (basestring)" % locals())
                return
            elif isinstance(field_value, int):
                if field_value == 0:
                    return
                raise NotImplementedError("%(field_name)s: %(field_value)s" % locals())
        elif field_metadata.type == dict:
            if existing_field_value is None:
                existing_field_value = {}
            assert field_number is not None
            assert not field_number in existing_field_value
            existing_field_value[field_number] = field_value
            # print(existing_field_value)
            return existing_field_value
            # raise NotImplementedError("%(field_name)s: %(field_value)s" % locals())
        elif field_metadata.type == str:
            if not isinstance(field_value, str):
                logging.info("converting %s=%s (%s) to string", field_name, field_value, type(field_value))
                return str(field_value)
            return field_value
        else:
            if hasattr(field_metadata.type, 'value_of'):
                try:
                    return field_metadata.type.value_of(str(field_value).upper().replace(' ', '_'))
                except ValueError as e:
                    field_value_type = type(field_value)
                    field_metadata_type = field_metadata.type
                    logging.warn("unable to convert %(field_name)s=%(field_value)s (%(field_value_type)s) to %(field_metadata_type)s: %(e)s" % locals())
                    return
            else:
                try:
                    return field_metadata.type(field_value)
                except (TypeError, ValueError) as e:
                    raise TypeError("unable to coerce %s=%s (%s) to a %s: %s" % (field_name, field_value, type(field_value), field_metadata.type, e))

    def _map_record(self, record):
        raise NotImplementedError

    def _map_record_field(self, field_name, field_value, struct_builder, struct_type):
        if field_value is None:
            return
        elif isinstance(field_value, str):
            field_value = field_value.strip()
            if len(field_value) == 0:
                return

        field_name_base = field_name
        field_number = None
        for i in range(2, 0, -1):
            try:
                field_number = int(field_name[-1 * i:])
                field_name_base = field_name[:-1 * i]
                break
            except ValueError:
                pass
        field_metadata = getattr(getattr(struct_type, 'FieldMetadata'), field_name_base.upper())

        existing_field_value = getattr(struct_builder, field_name_base)

        new_field_value = \
            self._coerce_record_field(
                existing_field_value=existing_field_value,
                field_number=field_number,
                field_metadata=field_metadata,
                field_value=field_value,
            )
        if new_field_value is None:
            return

        try:
            getattr(struct_builder, 'set_' + field_name_base)(new_field_value)
        except TypeError as e:
            raise TypeError("%(new_field_value)s: %(e)s" % locals())
        except ValueError as e:
            if field_metadata.validation is not None:
                return
            raise ValueError("%(new_field_value)s: %(e)s" % locals())

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwds):
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