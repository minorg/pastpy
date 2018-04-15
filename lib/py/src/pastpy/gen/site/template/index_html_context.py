import builtins
import pastpy.gen.site.site_metadata


class IndexHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            has_featured_searches=None,
            metadata=None,
        ):
            '''
            :type has_featured_searches: bool
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.__has_featured_searches = has_featured_searches
            self.__metadata = metadata

        def build(self):
            return IndexHtmlContext(has_featured_searches=self.__has_featured_searches, metadata=self.__metadata)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.index_html_context.IndexHtmlContext
            :rtype: pastpy.gen.site.template.index_html_context.IndexHtmlContext
            '''

            builder = cls()
            builder.has_featured_searches = template.has_featured_searches
            builder.metadata = template.metadata
            return builder

        @property
        def has_featured_searches(self):
            '''
            :rtype: bool
            '''

            return self.__has_featured_searches

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

        def set_has_featured_searches(self, has_featured_searches):
            '''
            :type has_featured_searches: bool
            '''

            if has_featured_searches is None:
                raise ValueError('has_featured_searches is required')
            if not isinstance(has_featured_searches, bool):
                raise TypeError("expected has_featured_searches to be a bool but it is a %s" % builtins.type(has_featured_searches))
            self.__has_featured_searches = has_featured_searches
            return self

        def set_metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            if metadata is None:
                raise ValueError('metadata is required')
            if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
                raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
            self.__metadata = metadata
            return self

        def update(self, index_html_context):
            '''
            :type has_featured_searches: bool
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            if isinstance(index_html_context, IndexHtmlContext):
                self.set_has_featured_searches(index_html_context.has_featured_searches)
                self.set_metadata(index_html_context.metadata)
            elif isinstance(index_html_context, dict):
                for key, value in index_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(index_html_context)
            return self

        @has_featured_searches.setter
        def has_featured_searches(self, has_featured_searches):
            '''
            :type has_featured_searches: bool
            '''

            self.set_has_featured_searches(has_featured_searches)

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

    class FieldMetadata(object):
        HAS_FEATURED_SEARCHES = None
        METADATA = None

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
            return (cls.HAS_FEATURED_SEARCHES, cls.METADATA,)

    FieldMetadata.HAS_FEATURED_SEARCHES = FieldMetadata('has_featured_searches', bool, None)
    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)

    def __init__(
        self,
        has_featured_searches,
        metadata,
    ):
        '''
        :type has_featured_searches: bool
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        if has_featured_searches is None:
            raise ValueError('has_featured_searches is required')
        if not isinstance(has_featured_searches, bool):
            raise TypeError("expected has_featured_searches to be a bool but it is a %s" % builtins.type(has_featured_searches))
        self.__has_featured_searches = has_featured_searches

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

    def __eq__(self, other):
        if self.has_featured_searches != other.has_featured_searches:
            return False
        if self.metadata != other.metadata:
            return False
        return True

    def __hash__(self):
        return hash((self.has_featured_searches, self.metadata,))

    def __iter__(self):
        return iter((self.has_featured_searches, self.metadata,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('has_featured_searches=' + repr(self.has_featured_searches))
        field_reprs.append('metadata=' + repr(self.metadata))
        return 'IndexHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('has_featured_searches=' + repr(self.has_featured_searches))
        field_reprs.append('metadata=' + repr(self.metadata))
        return 'IndexHtmlContext(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        has_featured_searches = _dict.get("has_featured_searches")
        if has_featured_searches is None:
            raise KeyError("has_featured_searches")
        __builder.has_featured_searches = has_featured_searches

        metadata = _dict.get("metadata")
        if metadata is None:
            raise KeyError("metadata")
        metadata = pastpy.gen.site.site_metadata.SiteMetadata.from_builtins(metadata)
        __builder.metadata = metadata

        return __builder.build()

    @property
    def has_featured_searches(self):
        '''
        :rtype: bool
        '''

        return self.__has_featured_searches

    @property
    def metadata(self):
        '''
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        return self.__metadata

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.index_html_context.IndexHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'has_featured_searches':
                init_kwds['has_featured_searches'] = iprot.read_bool()
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["has_featured_searches"] = self.has_featured_searches
        dict_["metadata"] = self.metadata.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.index_html_context.IndexHtmlContext
        '''

        oprot.write_struct_begin('IndexHtmlContext')

        oprot.write_field_begin(name='has_featured_searches', type=2, id=None)
        oprot.write_bool(self.has_featured_searches)
        oprot.write_field_end()

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
