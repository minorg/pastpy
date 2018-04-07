from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_metadata
import pastpy.gen.site.site_object
import pastpy.gen.site.site_pagination


class SiteObjectsList(object):
    class Builder(object):
        def __init__(
            self,
            absolute_href=None,
            metadata=None,
            objects=None,
            pagination=None,
        ):
            '''
            :type absolute_href: str
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            '''

            self.__absolute_href = absolute_href
            self.__metadata = metadata
            self.__objects = objects
            self.__pagination = pagination

        def build(self):
            return SiteObjectsList(absolute_href=self.__absolute_href, metadata=self.__metadata, objects=self.__objects, pagination=self.__pagination)

        @property
        def absolute_href(self):
            '''
            :rtype: str
            '''

            return self.__absolute_href

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_objects_list.SiteObjectsList
            :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
            '''

            builder = cls()
            builder.absolute_href = template.absolute_href
            builder.metadata = template.metadata
            builder.objects = template.objects
            builder.pagination = template.pagination
            return builder

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

        @property
        def objects(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            return self.__objects

        @property
        def pagination(self):
            '''
            :rtype: pastpy.gen.site.site_pagination.SitePagination
            '''

            return self.__pagination

        def set_absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            if absolute_href is None:
                raise ValueError('absolute_href is required')
            if not isinstance(absolute_href, str):
                raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
            self.__absolute_href = absolute_href
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

        def set_objects(self, objects):
            '''
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            if objects is None:
                raise ValueError('objects is required')
            if not (isinstance(objects, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_object.SiteObject), objects))) == 0):
                raise TypeError("expected objects to be a tuple(pastpy.gen.site.site_object.SiteObject) but it is a %s" % builtins.type(objects))
            self.__objects = objects
            return self

        def set_pagination(self, pagination):
            '''
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            '''

            if pagination is None:
                raise ValueError('pagination is required')
            if not isinstance(pagination, pastpy.gen.site.site_pagination.SitePagination):
                raise TypeError("expected pagination to be a pastpy.gen.site.site_pagination.SitePagination but it is a %s" % builtins.type(pagination))
            self.__pagination = pagination
            return self

        def update(self, site_objects_list):
            '''
            :type absolute_href: str
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            '''

            if isinstance(site_objects_list, SiteObjectsList):
                self.set_absolute_href(site_objects_list.absolute_href)
                self.set_metadata(site_objects_list.metadata)
                self.set_objects(site_objects_list.objects)
                self.set_pagination(site_objects_list.pagination)
            elif isinstance(site_objects_list, dict):
                for key, value in site_objects_list.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_objects_list)
            return self

        @absolute_href.setter
        def absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            self.set_absolute_href(absolute_href)

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

        @objects.setter
        def objects(self, objects):
            '''
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            self.set_objects(objects)

        @pagination.setter
        def pagination(self, pagination):
            '''
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            '''

            self.set_pagination(pagination)

    class FieldMetadata(object):
        ABSOLUTE_HREF = None
        METADATA = None
        OBJECTS = None
        PAGINATION = None

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
            return (cls.ABSOLUTE_HREF, cls.METADATA, cls.OBJECTS, cls.PAGINATION,)

    FieldMetadata.ABSOLUTE_HREF = FieldMetadata('absolute_href', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.PAGINATION = FieldMetadata('pagination', pastpy.gen.site.site_pagination.SitePagination, None)

    def __init__(
        self,
        absolute_href,
        metadata,
        objects,
        pagination,
    ):
        '''
        :type absolute_href: str
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type pagination: pastpy.gen.site.site_pagination.SitePagination
        '''

        if absolute_href is None:
            raise ValueError('absolute_href is required')
        if not isinstance(absolute_href, str):
            raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
        self.__absolute_href = absolute_href

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

        if objects is None:
            raise ValueError('objects is required')
        if not (isinstance(objects, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_object.SiteObject), objects))) == 0):
            raise TypeError("expected objects to be a tuple(pastpy.gen.site.site_object.SiteObject) but it is a %s" % builtins.type(objects))
        self.__objects = objects

        if pagination is None:
            raise ValueError('pagination is required')
        if not isinstance(pagination, pastpy.gen.site.site_pagination.SitePagination):
            raise TypeError("expected pagination to be a pastpy.gen.site.site_pagination.SitePagination but it is a %s" % builtins.type(pagination))
        self.__pagination = pagination

    def __eq__(self, other):
        if self.absolute_href != other.absolute_href:
            return False
        if self.metadata != other.metadata:
            return False
        if self.objects != other.objects:
            return False
        if self.pagination != other.pagination:
            return False
        return True

    def __hash__(self):
        return hash((self.absolute_href, self.metadata, self.objects, self.pagination,))

    def __iter__(self):
        return iter((self.absolute_href, self.metadata, self.objects, self.pagination,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('pagination=' + repr(self.pagination))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('pagination=' + repr(self.pagination))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

    @property
    def absolute_href(self):
        '''
        :rtype: str
        '''

        return self.__absolute_href

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        absolute_href = _dict.get("absolute_href")
        if absolute_href is None:
            raise KeyError("absolute_href")
        __builder.absolute_href = absolute_href

        metadata = _dict.get("metadata")
        if metadata is None:
            raise KeyError("metadata")
        metadata = pastpy.gen.site.site_metadata.SiteMetadata.from_builtins(metadata)
        __builder.metadata = metadata

        objects = _dict.get("objects")
        if objects is None:
            raise KeyError("objects")
        objects = tuple(pastpy.gen.site.site_object.SiteObject.from_builtins(element0) for element0 in objects)
        __builder.objects = objects

        pagination = _dict.get("pagination")
        if pagination is None:
            raise KeyError("pagination")
        pagination = pastpy.gen.site.site_pagination.SitePagination.from_builtins(pagination)
        __builder.pagination = pagination

        return __builder.build()

    @property
    def metadata(self):
        '''
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        return self.__metadata

    @property
    def objects(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
        '''

        return self.__objects

    @property
    def pagination(self):
        '''
        :rtype: pastpy.gen.site.site_pagination.SitePagination
        '''

        return self.__pagination

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'absolute_href':
                init_kwds['absolute_href'] = iprot.read_string()
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'pagination':
                init_kwds['pagination'] = pastpy.gen.site.site_pagination.SitePagination.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["absolute_href"] = self.absolute_href
        dict_["metadata"] = self.metadata.to_builtins()
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["pagination"] = self.pagination.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
        '''

        oprot.write_struct_begin('SiteObjectsList')

        oprot.write_field_begin(name='absolute_href', type=11, id=None)
        oprot.write_string(self.absolute_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='objects', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects))
        for _0 in self.objects:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='pagination', type=12, id=None)
        self.pagination.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
