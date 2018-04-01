from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_object
import pastpy.gen.site.site_objects_list


class SiteSitemap(object):
    class Builder(object):
        def __init__(
            self,
            lastmod=None,
            objects=None,
            objects_list_pages=None,
        ):
            '''
            :type lastmod: str
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type objects_list_pages: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
            '''

            self.__lastmod = lastmod
            self.__objects = objects
            self.__objects_list_pages = objects_list_pages

        def build(self):
            return SiteSitemap(lastmod=self.__lastmod, objects=self.__objects, objects_list_pages=self.__objects_list_pages)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_sitemap.SiteSitemap
            :rtype: pastpy.gen.site.site_sitemap.SiteSitemap
            '''

            builder = cls()
            builder.lastmod = template.lastmod
            builder.objects = template.objects
            builder.objects_list_pages = template.objects_list_pages
            return builder

        @property
        def lastmod(self):
            '''
            :rtype: str
            '''

            return self.__lastmod

        @property
        def objects(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            return self.__objects

        @property
        def objects_list_pages(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
            '''

            return self.__objects_list_pages

        def set_lastmod(self, lastmod):
            '''
            :type lastmod: str
            '''

            if lastmod is None:
                raise ValueError('lastmod is required')
            if not isinstance(lastmod, str):
                raise TypeError("expected lastmod to be a str but it is a %s" % builtins.type(lastmod))
            self.__lastmod = lastmod
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

        def set_objects_list_pages(self, objects_list_pages):
            '''
            :type objects_list_pages: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
            '''

            if objects_list_pages is None:
                raise ValueError('objects_list_pages is required')
            if not (isinstance(objects_list_pages, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list.SiteObjectsList), objects_list_pages))) == 0):
                raise TypeError("expected objects_list_pages to be a tuple(pastpy.gen.site.site_objects_list.SiteObjectsList) but it is a %s" % builtins.type(objects_list_pages))
            self.__objects_list_pages = objects_list_pages
            return self

        def update(self, site_sitemap):
            '''
            :type lastmod: str
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type objects_list_pages: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
            '''

            if isinstance(site_sitemap, SiteSitemap):
                self.set_lastmod(site_sitemap.lastmod)
                self.set_objects(site_sitemap.objects)
                self.set_objects_list_pages(site_sitemap.objects_list_pages)
            elif isinstance(site_sitemap, dict):
                for key, value in site_sitemap.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_sitemap)
            return self

        @lastmod.setter
        def lastmod(self, lastmod):
            '''
            :type lastmod: str
            '''

            self.set_lastmod(lastmod)

        @objects.setter
        def objects(self, objects):
            '''
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            self.set_objects(objects)

        @objects_list_pages.setter
        def objects_list_pages(self, objects_list_pages):
            '''
            :type objects_list_pages: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
            '''

            self.set_objects_list_pages(objects_list_pages)

    class FieldMetadata(object):
        LASTMOD = None
        OBJECTS = None
        OBJECTS_LIST_PAGES = None

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
            return (cls.LASTMOD, cls.OBJECTS, cls.OBJECTS_LIST_PAGES,)

    FieldMetadata.LASTMOD = FieldMetadata('lastmod', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.OBJECTS_LIST_PAGES = FieldMetadata('objects_list_pages', tuple, None)

    def __init__(
        self,
        lastmod,
        objects,
        objects_list_pages,
    ):
        '''
        :type lastmod: str
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type objects_list_pages: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
        '''

        if lastmod is None:
            raise ValueError('lastmod is required')
        if not isinstance(lastmod, str):
            raise TypeError("expected lastmod to be a str but it is a %s" % builtins.type(lastmod))
        self.__lastmod = lastmod

        if objects is None:
            raise ValueError('objects is required')
        if not (isinstance(objects, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_object.SiteObject), objects))) == 0):
            raise TypeError("expected objects to be a tuple(pastpy.gen.site.site_object.SiteObject) but it is a %s" % builtins.type(objects))
        self.__objects = objects

        if objects_list_pages is None:
            raise ValueError('objects_list_pages is required')
        if not (isinstance(objects_list_pages, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list.SiteObjectsList), objects_list_pages))) == 0):
            raise TypeError("expected objects_list_pages to be a tuple(pastpy.gen.site.site_objects_list.SiteObjectsList) but it is a %s" % builtins.type(objects_list_pages))
        self.__objects_list_pages = objects_list_pages

    def __eq__(self, other):
        if self.lastmod != other.lastmod:
            return False
        if self.objects != other.objects:
            return False
        if self.objects_list_pages != other.objects_list_pages:
            return False
        return True

    def __hash__(self):
        return hash((self.lastmod, self.objects, self.objects_list_pages,))

    def __iter__(self):
        return iter((self.lastmod, self.objects, self.objects_list_pages,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('lastmod=' + "'" + self.lastmod.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('objects_list_pages=' + repr(self.objects_list_pages))
        return 'SiteSitemap(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('lastmod=' + "'" + self.lastmod.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('objects_list_pages=' + repr(self.objects_list_pages))
        return 'SiteSitemap(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        lastmod = _dict.get("lastmod")
        if lastmod is None:
            raise KeyError("lastmod")
        __builder.lastmod = lastmod

        objects = _dict.get("objects")
        if objects is None:
            raise KeyError("objects")
        objects = tuple(pastpy.gen.site.site_object.SiteObject.from_builtins(element0) for element0 in objects)
        __builder.objects = objects

        objects_list_pages = _dict.get("objects_list_pages")
        if objects_list_pages is None:
            raise KeyError("objects_list_pages")
        objects_list_pages = tuple(pastpy.gen.site.site_objects_list.SiteObjectsList.from_builtins(element0) for element0 in objects_list_pages)
        __builder.objects_list_pages = objects_list_pages

        return __builder.build()

    @property
    def lastmod(self):
        '''
        :rtype: str
        '''

        return self.__lastmod

    @property
    def objects(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
        '''

        return self.__objects

    @property
    def objects_list_pages(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_objects_list.SiteObjectsList)
        '''

        return self.__objects_list_pages

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_sitemap.SiteSitemap
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'lastmod':
                init_kwds['lastmod'] = iprot.read_string()
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'objects_list_pages':
                init_kwds['objects_list_pages'] = tuple([pastpy.gen.site.site_objects_list.SiteObjectsList.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["lastmod"] = self.lastmod
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["objects_list_pages"] = tuple(element0.to_builtins() for element0 in self.objects_list_pages)
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_sitemap.SiteSitemap
        '''

        oprot.write_struct_begin('SiteSitemap')

        oprot.write_field_begin(name='lastmod', type=11, id=None)
        oprot.write_string(self.lastmod)
        oprot.write_field_end()

        oprot.write_field_begin(name='objects', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects))
        for _0 in self.objects:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='objects_list_pages', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects_list_pages))
        for _0 in self.objects_list_pages:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
