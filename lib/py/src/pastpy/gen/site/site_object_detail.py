import builtins
import pastpy.gen.site.site_object


class SiteObjectDetail(object):
    class Builder(object):
        def __init__(
            self,
            object=None,  # @ReservedAssignment
        ):
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            self.__object = object

        def build(self):
            return SiteObjectDetail(object=self.__object)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_object_detail.SiteObjectDetail
            :rtype: pastpy.gen.site.site_object_detail.SiteObjectDetail
            '''

            builder = cls()
            builder.object = template.object
            return builder

        @property
        def object(self):  # @ReservedAssignment
            '''
            :rtype: pastpy.gen.site.site_object.SiteObject
            '''

            return self.__object

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

        def update(self, site_object_detail):
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            if isinstance(site_object_detail, SiteObjectDetail):
                self.set_object(site_object_detail.object)
            elif isinstance(site_object_detail, dict):
                for key, value in site_object_detail.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_object_detail)
            return self

        @object.setter
        def object(self, object):  # @ReservedAssignment
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            self.set_object(object)

    class FieldMetadata(object):
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
            return (cls.OBJECT,)

    FieldMetadata.OBJECT = FieldMetadata('object', pastpy.gen.site.site_object.SiteObject, None)

    def __init__(
        self,
        object,  # @ReservedAssignment
    ):
        '''
        :type object: pastpy.gen.site.site_object.SiteObject
        '''

        if object is None:
            raise ValueError('object is required')
        if not isinstance(object, pastpy.gen.site.site_object.SiteObject):
            raise TypeError("expected object to be a pastpy.gen.site.site_object.SiteObject but it is a %s" % builtins.type(object))
        self.__object = object

    def __eq__(self, other):
        if self.object != other.object:
            return False
        return True

    def __hash__(self):
        return hash(self.object)

    def __iter__(self):
        return iter((self.object,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('object=' + repr(self.object))
        return 'SiteObjectDetail(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('object=' + repr(self.object))
        return 'SiteObjectDetail(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        object = _dict.get("object")
        if object is None:
            raise KeyError("object")
        object = pastpy.gen.site.site_object.SiteObject.from_builtins(object)
        __builder.object = object

        return __builder.build()

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
        :rtype: pastpy.gen.site.site_object_detail.SiteObjectDetail
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'object':
                init_kwds['object'] = pastpy.gen.site.site_object.SiteObject.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["object"] = self.object.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_object_detail.SiteObjectDetail
        '''

        oprot.write_struct_begin('SiteObjectDetail')

        oprot.write_field_begin(name='object', type=12, id=None)
        self.object.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
