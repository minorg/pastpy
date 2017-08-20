import dbf
import os.path


THRIFT_DIR_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'src', 'pastpy', 'models')


class RecordField(object):
    THRIFT_IMPORTS_BY_TYPE = {
        'date_time.DateTime': 'include "thryft/native/date_time.thrift"',
        'decimal.Decimal': 'include "thryft/native/decimal.thrift"',
    }

    # DBF type is C for char, et al.
    # http://dbfread.readthedocs.io/en/latest/field_types.html
    THRIFT_TYPE_BY_DBF_TYPE = {
        # C	text	unicode string
        'C': 'string',

        # D	date	datetime.date or None
        'D': 'date_time.DateTime',

        # L	logical	True, False or None
        'L': 'bool',

        # M	memo	unicode string (memo), byte string (picture or object) or None
        'M': 'string',

        # N	numeric	int, float or None
        'N': 'decimal.Decimal',

        # T	time	datetime.datetime
        'T': 'date_time.DateTime',
    }

    def __init__(self, dbf_field_info, name):
        self.__dbf_field_info = dbf_field_info
        self.__name = name

        dbf_type = chr(dbf_field_info.field_type)
        if dbf_type == 'N':
            if dbf_field_info.decimal > 0:
                thrift_type = 'decimal.Decimal'
            else:
                thrift_type = 'i32'
        else:
            thrift_type = self.THRIFT_TYPE_BY_DBF_TYPE[dbf_type]
        self.__thrift_type = thrift_type

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.thrift_type != other.thrift_type:
            return False
        return True

    @property
    def name(self):
        return self.__name

    def thrift_import(self):
        return self.THRIFT_IMPORTS_BY_TYPE.get(self.thrift_type, None)

    def thrift_repr(self):
        dbf_type = [chr(self.__dbf_field_info.field_type)]
        if self.__dbf_field_info.length > 0:
            dbf_type.append(str(self.__dbf_field_info.length))
        if self.__dbf_field_info.decimal > 0:
            dbf_type.append(str(self.__dbf_field_info.decimal))
        dbf_type = ','.join(dbf_type)
        name = self.name
        thrift_type = self.thrift_type
        return """\
    // %(dbf_type)s
    optional %(thrift_type)s %(name)s;""" % locals()

    @property
    def thrift_type(self):
        return self.__thrift_type


def generate_record_thrift(union_dbf_file_paths, thrift_file_name):
    fields_by_name = {}
    thrift_imports = []
    for dbf_file_path in union_dbf_file_paths:
        with dbf.Table(dbf_file_path) as table:
            for field_name in table.field_names:
                field = RecordField(dbf_field_info=table.field_info(
                    field_name), name=field_name)
                if field_name in fields_by_name:
                    assert field == fields_by_name[field_name]
                fields_by_name[field_name] = field
                thrift_import = field.thrift_import()
                if thrift_import is not None and thrift_import not in thrift_imports:
                    thrift_imports.append(thrift_import)

    field_thrift_reprs = []
    for field_name in sorted(fields_by_name.keys()):
        field_thrift_reprs.append(fields_by_name[field_name].thrift_repr())
    field_thrift_reprs = "\n\n".join(field_thrift_reprs)
    thrift_file_path = os.path.join(THRIFT_DIR_PATH, thrift_file_name)

    thrift_imports = "\n".join(sorted(thrift_imports))

    struct_name = ''.join(part.capitalize()
                          for part in os.path.splitext(thrift_file_name)[0].split('_'))
    with open(thrift_file_path, 'w+b') as thrift_file:
        thrift_file.write(("""\
namespace * pastpy.models

%(thrift_imports)s

struct %(struct_name)s {
%(field_thrift_reprs)s
}
""" % locals()).replace("\r\n", "\n").encode("ascii"))
        print('wrote', thrift_file_path)


assert __name__ == '__main__'

generate_record_thrift(("C:\\pp5eval\\Data\\OBJECTS.DBF", "C:\\pp5Reports\\PPSdata.dbf",),
                       'object_record.thrift')
