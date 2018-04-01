import builtins
import pastpy.gen.non_blank_string


class SiteFeaturedSearch(object):
    class Builder(object):
        def __init__(
            self,
            name=None,
            query=None,
        ):
            '''
            :type name: str
            :type query: str
            '''

            self.__name = name
            self.__query = query

        def build(self):
            return SiteFeaturedSearch(name=self.__name, query=self.__query)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_featured_search.SiteFeaturedSearch
            :rtype: pastpy.gen.site.site_featured_search.SiteFeaturedSearch
            '''

            builder = cls()
            builder.name = template.name
            builder.query = template.query
            return builder

        @property
        def name(self):
            '''
            :rtype: str
            '''

            return self.__name

        @property
        def query(self):
            '''
            :rtype: str
            '''

            return self.__query

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

        def set_query(self, query):
            '''
            :type query: str
            '''

            if query is None:
                raise ValueError('query is required')
            if not isinstance(query, str):
                raise TypeError("expected query to be a str but it is a %s" % builtins.type(query))
            self.__query = query
            return self

        def update(self, site_featured_search):
            '''
            :type name: str
            :type query: str
            '''

            if isinstance(site_featured_search, SiteFeaturedSearch):
                self.set_name(site_featured_search.name)
                self.set_query(site_featured_search.query)
            elif isinstance(site_featured_search, dict):
                for key, value in site_featured_search.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_featured_search)
            return self

        @name.setter
        def name(self, name):
            '''
            :type name: str
            '''

            self.set_name(name)

        @query.setter
        def query(self, query):
            '''
            :type query: str
            '''

            self.set_query(query)

    class FieldMetadata(object):
        NAME = None
        QUERY = None

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
            return (cls.NAME, cls.QUERY,)

    FieldMetadata.NAME = FieldMetadata('name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.QUERY = FieldMetadata('query', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        name,
        query,
    ):
        '''
        :type name: str
        :type query: str
        '''

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, str):
            raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
        self.__name = name

        if query is None:
            raise ValueError('query is required')
        if not isinstance(query, str):
            raise TypeError("expected query to be a str but it is a %s" % builtins.type(query))
        self.__query = query

    def __eq__(self, other):
        if self.name != other.name:
            return False
        if self.query != other.query:
            return False
        return True

    def __hash__(self):
        return hash((self.name, self.query,))

    def __iter__(self):
        return iter((self.name, self.query,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('query=' + "'" + self.query.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteFeaturedSearch(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('query=' + "'" + self.query.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteFeaturedSearch(' + ', '.join(field_reprs) + ')'

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

        query = _dict.get("query")
        if query is None:
            raise KeyError("query")
        __builder.query = query

        return __builder.build()

    @property
    def name(self):
        '''
        :rtype: str
        '''

        return self.__name

    @property
    def query(self):
        '''
        :rtype: str
        '''

        return self.__query

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_featured_search.SiteFeaturedSearch
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'query':
                init_kwds['query'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["name"] = self.name
        dict_["query"] = self.query
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_featured_search.SiteFeaturedSearch
        '''

        oprot.write_struct_begin('SiteFeaturedSearch')

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='query', type=11, id=None)
        oprot.write_string(self.query)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
