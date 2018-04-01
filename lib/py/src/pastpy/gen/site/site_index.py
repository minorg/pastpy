import builtins
import pastpy.gen.site.site_metadata


class SiteIndex(object):
    class Builder(object):
        def __init__(
            self,
            metadata=None,
        ):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.__metadata = metadata

        def build(self):
            return SiteIndex(metadata=self.__metadata)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_index.SiteIndex
            :rtype: pastpy.gen.site.site_index.SiteIndex
            '''

            builder = cls()
            builder.metadata = template.metadata
            return builder

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

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

        def update(self, site_index):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            if isinstance(site_index, SiteIndex):
                self.set_metadata(site_index.metadata)
            elif isinstance(site_index, dict):
                for key, value in site_index.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_index)
            return self

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

    class FieldMetadata(object):
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
            return (cls.METADATA,)

    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)

    def __init__(
        self,
        metadata,
    ):
        '''
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

    def __eq__(self, other):
        if self.metadata != other.metadata:
            return False
        return True

    def __hash__(self):
        return hash(self.metadata)

    def __iter__(self):
        return iter((self.metadata,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        return 'SiteIndex(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        return 'SiteIndex(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        metadata = _dict.get("metadata")
        if metadata is None:
            raise KeyError("metadata")
        metadata = pastpy.gen.site.site_metadata.SiteMetadata.from_builtins(metadata)
        __builder.metadata = metadata

        return __builder.build()

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
        :rtype: pastpy.gen.site.site_index.SiteIndex
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["metadata"] = self.metadata.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_index.SiteIndex
        '''

        oprot.write_struct_begin('SiteIndex')

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
