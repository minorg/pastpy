import builtins
import pastpy.gen.site.site_metadata
import pastpy.gen.site.site_object


class ObjectDetailHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            metadata=None,
            object=None,  # @ReservedAssignment
        ):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            self.__metadata = metadata
            self.__object = object

        def build(self):
            return ObjectDetailHtmlContext(metadata=self.__metadata, object=self.__object)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
            :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
            '''

            builder = cls()
            builder.metadata = template.metadata
            builder.object = template.object
            return builder

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

        @property
        def object(self):  # @ReservedAssignment
            '''
            :rtype: pastpy.gen.site.site_object.SiteObject
            '''

            return self.__object

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

        def set_object(self, object):  # @ReservedAssignment
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            if object is None:
                raise ValueError('object is required')
            if not isinstance(object, pastpy.gen.site.site_object.SiteObject):
                raise TypeError("expected object to be a pastpy.gen.site.site_object.SiteObject but it is a %s" % builtins.type(object))
            self.__object = object
            return self

        def update(self, object_detail_html_context):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            if isinstance(object_detail_html_context, ObjectDetailHtmlContext):
                self.set_metadata(object_detail_html_context.metadata)
                self.set_object(object_detail_html_context.object)
            elif isinstance(object_detail_html_context, dict):
                for key, value in object_detail_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(object_detail_html_context)
            return self

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

        @object.setter
        def object(self, object):  # @ReservedAssignment
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            self.set_object(object)

    class FieldMetadata(object):
        METADATA = None
        OBJECT = None

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
            return (cls.METADATA, cls.OBJECT,)

    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)
    FieldMetadata.OBJECT = FieldMetadata('object', pastpy.gen.site.site_object.SiteObject, None)

    def __init__(
        self,
        metadata,
        object,  # @ReservedAssignment
    ):
        '''
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        :type object: pastpy.gen.site.site_object.SiteObject
        '''

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

        if object is None:
            raise ValueError('object is required')
        if not isinstance(object, pastpy.gen.site.site_object.SiteObject):
            raise TypeError("expected object to be a pastpy.gen.site.site_object.SiteObject but it is a %s" % builtins.type(object))
        self.__object = object

    def __eq__(self, other):
        if self.metadata != other.metadata:
            return False
        if self.object != other.object:
            return False
        return True

    def __hash__(self):
        return hash((self.metadata, self.object,))

    def __iter__(self):
        return iter((self.metadata, self.object,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('object=' + repr(self.object))
        return 'ObjectDetailHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('object=' + repr(self.object))
        return 'ObjectDetailHtmlContext(' + ', '.join(field_reprs) + ')'

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

        object = _dict.get("object")
        if object is None:
            raise KeyError("object")
        object = pastpy.gen.site.site_object.SiteObject.from_builtins(object)
        __builder.object = object

        return __builder.build()

    @property
    def metadata(self):
        '''
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        return self.__metadata

    @property
    def object(self):  # @ReservedAssignment
        '''
        :rtype: pastpy.gen.site.site_object.SiteObject
        '''

        return self.__object

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            elif ifield_name == 'object':
                init_kwds['object'] = pastpy.gen.site.site_object.SiteObject.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["metadata"] = self.metadata.to_builtins()
        dict_["object"] = self.object.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
        '''

        oprot.write_struct_begin('ObjectDetailHtmlContext')

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='object', type=12, id=None)
        self.object.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
