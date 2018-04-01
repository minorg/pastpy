import builtins
import pastpy.gen.non_blank_string


class SiteKeyValuePair(object):
    class Builder(object):
        def __init__(
            self,
            key=None,
            value=None,
        ):
            '''
            :type key: str
            :type value: object
            '''

            self.__key = key
            self.__value = value

        def build(self):
            return SiteKeyValuePair(key=self.__key, value=self.__value)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_key_value_pair.SiteKeyValuePair
            :rtype: pastpy.gen.site.site_key_value_pair.SiteKeyValuePair
            '''

            builder = cls()
            builder.key = template.key
            builder.value = template.value
            return builder

        @property
        def key(self):
            '''
            :rtype: str
            '''

            return self.__key

        def set_key(self, key):
            '''
            :type key: str
            '''

            if key is None:
                raise ValueError('key is required')
            if not isinstance(key, str):
                raise TypeError("expected key to be a str but it is a %s" % builtins.type(key))
            self.__key = key
            return self

        def set_value(self, value):
            '''
            :type value: object
            '''

            if value is None:
                raise ValueError('value is required')
            self.__value = value
            return self

        def update(self, site_key_value_pair):
            '''
            :type key: str
            :type value: object
            '''

            if isinstance(site_key_value_pair, SiteKeyValuePair):
                self.set_key(site_key_value_pair.key)
                self.set_value(site_key_value_pair.value)
            elif isinstance(site_key_value_pair, dict):
                for key, value in site_key_value_pair.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_key_value_pair)
            return self

        @property
        def value(self):
            '''
            :rtype: object
            '''

            return self.__value

        @key.setter
        def key(self, key):
            '''
            :type key: str
            '''

            self.set_key(key)

        @value.setter
        def value(self, value):
            '''
            :type value: object
            '''

            self.set_value(value)

    class FieldMetadata(object):
        KEY = None
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
            return (cls.KEY, cls.VALUE,)

    FieldMetadata.KEY = FieldMetadata('key', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.VALUE = FieldMetadata('value', object, None)

    def __init__(
        self,
        key,
        value,
    ):
        '''
        :type key: str
        :type value: object
        '''

        if key is None:
            raise ValueError('key is required')
        if not isinstance(key, str):
            raise TypeError("expected key to be a str but it is a %s" % builtins.type(key))
        self.__key = key

        if value is None:
            raise ValueError('value is required')

        self.__value = value

    def __eq__(self, other):
        if self.key != other.key:
            return False
        if self.value != other.value:
            return False
        return True

    def __hash__(self):
        return hash((self.key, self.value,))

    def __iter__(self):
        return iter((self.key, self.value,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('key=' + "'" + self.key.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('value=' + "'" + self.value.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteKeyValuePair(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('key=' + "'" + self.key.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('value=' + "'" + self.value.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteKeyValuePair(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        key = _dict.get("key")
        if key is None:
            raise KeyError("key")
        __builder.key = key

        value = _dict.get("value")
        if value is None:
            raise KeyError("value")
        __builder.value = value

        return __builder.build()

    @property
    def key(self):
        '''
        :rtype: str
        '''

        return self.__key

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_key_value_pair.SiteKeyValuePair
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'key':
                init_kwds['key'] = iprot.read_string()
            elif ifield_name == 'value':
                init_kwds['value'] = iprot.read_variant()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["key"] = self.key
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
        :rtype: pastpy.gen.site.site_key_value_pair.SiteKeyValuePair
        '''

        oprot.write_struct_begin('SiteKeyValuePair')

        oprot.write_field_begin(name='key', type=11, id=None)
        oprot.write_string(self.key)
        oprot.write_field_end()

        oprot.write_field_begin(name='value', type=11, id=None)
        oprot.write_variant(self.value)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
