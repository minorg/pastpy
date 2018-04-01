import builtins
import pastpy.gen.non_blank_string


class SiteAttribute(object):
    class Builder(object):
        def __init__(
            self,
            name=None,
            value=None,
        ):
            '''
            :type name: str
            :type value: object
            '''

            self.__name = name
            self.__value = value

        def build(self):
            return SiteAttribute(name=self.__name, value=self.__value)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_attribute.SiteAttribute
            :rtype: pastpy.gen.site.site_attribute.SiteAttribute
            '''

            builder = cls()
            builder.name = template.name
            builder.value = template.value
            return builder

        @property
        def name(self):
            '''
            :rtype: str
            '''

            return self.__name

        def set_name(self, name):
            '''
            :type name: str
            '''

            if name is None:
                raise ValueError('name is required')
            if not isinstance(name, str):
                raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
            self.__name = name
            return self

        def set_value(self, value):
            '''
            :type value: object
            '''

            if value is None:
                raise ValueError('value is required')
            self.__value = value
            return self

        def update(self, site_attribute):
            '''
            :type name: str
            :type value: object
            '''

            if isinstance(site_attribute, SiteAttribute):
                self.set_name(site_attribute.name)
                self.set_value(site_attribute.value)
            elif isinstance(site_attribute, dict):
                for key, value in site_attribute.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_attribute)
            return self

        @property
        def value(self):
            '''
            :rtype: object
            '''

            return self.__value

        @name.setter
        def name(self, name):
            '''
            :type name: str
            '''

            self.set_name(name)

        @value.setter
        def value(self, value):
            '''
            :type value: object
            '''

            self.set_value(value)

    class FieldMetadata(object):
        NAME = None
        VALUE = None

        def __init__(self, name, type_, validation):
            object.__init__(self)
            self.__name = name
            self.__type = type_
            self.__validation = validation

        @property
        def name(self):
            return self.__name

        def __repr__(self):
            return self.__name

        def __str__(self):
            return self.__name

        @property
        def type(self):
            return self.__type

        @property
        def validation(self):
            return self.__validation

        @classmethod
        def values(cls):
            return (cls.NAME, cls.VALUE,)

    FieldMetadata.NAME = FieldMetadata('name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.VALUE = FieldMetadata('value', object, None)

    def __init__(
        self,
        name,
        value,
    ):
        '''
        :type name: str
        :type value: object
        '''

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, str):
            raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
        self.__name = name

        if value is None:
            raise ValueError('value is required')

        self.__value = value

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.value != other.value:
            return False
        return True

    def __hash__(self):
        return hash((self.name, self.value,))

    def __iter__(self):
        return iter((self.name, self.value,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('value=' + "'" + self.value.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteAttribute(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('value=' + "'" + self.value.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteAttribute(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        name = _dict.get("name")
        if name is None:
            raise KeyError("name")
        __builder.name = name

        value = _dict.get("value")
        if value is None:
            raise KeyError("value")
        __builder.value = value

        return __builder.build()

    @property
    def name(self):
        '''
        :rtype: str
        '''

        return self.__name

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_attribute.SiteAttribute
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'value':
                init_kwds['value'] = iprot.read_variant()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["name"] = self.name
        dict_["value"] = self.value
        return dict_

    @property
    def value(self):
        '''
        :rtype: object
        '''

        return self.__value

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_attribute.SiteAttribute
        '''

        oprot.write_struct_begin('SiteAttribute')

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='value', type=11, id=None)
        oprot.write_variant(self.value)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
