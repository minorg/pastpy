from itertools import filterfalse
import builtins
import pastpy.gen.site.site_metadata
import pastpy.gen.site.site_objects_list_page


class SiteObjectsList(object):
    class Builder(object):
        def __init__(
            self,
            metadata=None,
            pages=None,
        ):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type pages: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
            '''

            self.__metadata = metadata
            self.__pages = pages

        def build(self):
            return SiteObjectsList(metadata=self.__metadata, pages=self.__pages)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_objects_list.SiteObjectsList
            :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
            '''

            builder = cls()
            builder.metadata = template.metadata
            builder.pages = template.pages
            return builder

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

        @property
        def pages(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
            '''

            return self.__pages

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

        def set_pages(self, pages):
            '''
            :type pages: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
            '''

            if pages is None:
                raise ValueError('pages is required')
            if not (isinstance(pages, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page.SiteObjectsListPage), pages))) == 0):
                raise TypeError("expected pages to be a tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage) but it is a %s" % builtins.type(pages))
            self.__pages = pages
            return self

        def update(self, site_objects_list):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type pages: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
            '''

            if isinstance(site_objects_list, SiteObjectsList):
                self.set_metadata(site_objects_list.metadata)
                self.set_pages(site_objects_list.pages)
            elif isinstance(site_objects_list, dict):
                for key, value in site_objects_list.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_objects_list)
            return self

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

        @pages.setter
        def pages(self, pages):
            '''
            :type pages: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
            '''

            self.set_pages(pages)

    class FieldMetadata(object):
        METADATA = None
        PAGES = None

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
            return (cls.METADATA, cls.PAGES,)

    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)
    FieldMetadata.PAGES = FieldMetadata('pages', tuple, None)

    def __init__(
        self,
        metadata,
        pages,
    ):
        '''
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        :type pages: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
        '''

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

        if pages is None:
            raise ValueError('pages is required')
        if not (isinstance(pages, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page.SiteObjectsListPage), pages))) == 0):
            raise TypeError("expected pages to be a tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage) but it is a %s" % builtins.type(pages))
        self.__pages = pages

    def __eq__(self, other):
        if self.metadata != other.metadata:
            return False
        if self.pages != other.pages:
            return False
        return True

    def __hash__(self):
        return hash((self.metadata, self.pages,))

    def __iter__(self):
        return iter((self.metadata, self.pages,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('pages=' + repr(self.pages))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('pages=' + repr(self.pages))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

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

        pages = _dict.get("pages")
        if pages is None:
            raise KeyError("pages")
        pages = tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage.from_builtins(element0) for element0 in pages)
        __builder.pages = pages

        return __builder.build()

    @property
    def metadata(self):
        '''
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        return self.__metadata

    @property
    def pages(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_objects_list_page.SiteObjectsListPage)
        '''

        return self.__pages

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
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            elif ifield_name == 'pages':
                init_kwds['pages'] = tuple([pastpy.gen.site.site_objects_list_page.SiteObjectsListPage.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["metadata"] = self.metadata.to_builtins()
        dict_["pages"] = tuple(element0.to_builtins() for element0 in self.pages)
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
        '''

        oprot.write_struct_begin('SiteObjectsList')

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='pages', type=15, id=None)
        oprot.write_list_begin(12, len(self.pages))
        for _0 in self.pages:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
