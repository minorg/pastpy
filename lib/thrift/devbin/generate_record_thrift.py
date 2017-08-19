import dbf
import os.path


THRIFT_DIR_PATH = os.path.join(os.path.dirname(
    __file__), '..', 'src', 'pastpy', 'models')


class RecordField(object):
    # DBF type is C for char, et al.
    # http://dbfread.readthedocs.io/en/latest/field_types.html
    THRIFT_TYPE_BY_DBF_TYPE = {
        'C': 'string'
    }

    def __init__(self, dbf_field_info, name):
        self.__dbf_field_info = dbf_field_info
        self.__name = name

        dbf_type = chr(dbf_field_info.field_type)
        self.__thrift_type = self.THRIFT_TYPE_BY_DBF_TYPE[dbf_type]

        # field_length = field_info.length
        # field_decimal = field_info.decimal
        # field_py_type = field_info.py_type

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.thrift_type != other.thrift_type:
            return False
        return True

    @property
    def name(self):
        return self.__name

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
    optional %(thrift_type)s %(name)s;""" % locals()

    @property
    def thrift_type(self):
        return self.__thrift_type


def generate_record_thrift(union_dbf_file_paths, thrift_file_name):
    fields_by_name = {}
    for dbf_file_path in union_dbf_file_paths:
        with dbf.Table(dbf_file_path) as table:
            for field_name in table.field_names:
                field = RecordField(dbf_field_info=table.field_info(
                    field_name), name=field_name)
                if field_name in fields_by_name:
                    assert field == fields_by_name[field_name]
                fields_by_name[field_name] = field

    field_thrift_reprs = []
    for field_name in sorted(fields_by_name.keys()):
        field_thrift_reprs.append(fields_by_name[field_name].thrift_repr())
    field_thrift_reprs = "\n\n".join(field_thrift_reprs)
    thrift_file_path = os.path.join(THRIFT_DIR_PATH, thrift_file_name)

    struct_name = ''.join(part.capitalize()
                          for part in os.path.splitext(thrift_file_name)[0].split('_'))
    with open(thrift_file_path, 'w+') as thrift_file:
        thrift_file.write(("""\
namespace * pastpy.models

struct %(struct_name)s {
}""" % locals()).encode("ascii"))
        print('wrote', thrift_file_path)


assert __name__ == '__main__'

generate_record_thrift(("C:\\pp5eval\\Data\\OBJECTS.DBF", "C:\\pp5Reports\\PPSdata.dbf",),
                       'object_record.thrift')
