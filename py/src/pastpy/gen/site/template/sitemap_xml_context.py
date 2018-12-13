from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_configuration
import pastpy.gen.site.site_object
import pastpy.gen.site.site_pagination_page_number


class SitemapXmlContext(object):
    class Builder(object):
        def __init__(
            self,
            configuration=None,
            lastmod=None,
            objects=None,
            objects_list_page_numbers=None,
        ):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type lastmod: str
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type objects_list_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            self.__configuration = configuration
            self.__lastmod = lastmod
            self.__objects = objects
            self.__objects_list_page_numbers = objects_list_page_numbers

        def build(self):
            return SitemapXmlContext(configuration=self.__configuration, lastmod=self.__lastmod, objects=self.__objects, objects_list_page_numbers=self.__objects_list_page_numbers)

        @property
        def configuration(self):
            '''
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            return self.__configuration

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.sitemap_xml_context.SitemapXmlContext
            :rtype: pastpy.gen.site.template.sitemap_xml_context.SitemapXmlContext
            '''

            builder = cls()
            builder.configuration = template.configuration
            builder.lastmod = template.lastmod
            builder.objects = template.objects
            builder.objects_list_page_numbers = template.objects_list_page_numbers
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
        def objects_list_page_numbers(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            return self.__objects_list_page_numbers

        def set_configuration(self, configuration):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            if configuration is None:
                raise ValueError('configuration is required')
            if not isinstance(configuration, pastpy.gen.site.site_configuration.SiteConfiguration):
                raise TypeError("expected configuration to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(configuration))
            self.__configuration = configuration
            return self

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

        def set_objects_list_page_numbers(self, objects_list_page_numbers):
            '''
            :type objects_list_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            if objects_list_page_numbers is None:
                raise ValueError('objects_list_page_numbers is required')
            if not (isinstance(objects_list_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber), objects_list_page_numbers))) == 0):
                raise TypeError("expected objects_list_page_numbers to be a tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber) but it is a %s" % builtins.type(objects_list_page_numbers))
            self.__objects_list_page_numbers = objects_list_page_numbers
            return self

        def update(self, sitemap_xml_context):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type lastmod: str
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type objects_list_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            if isinstance(sitemap_xml_context, SitemapXmlContext):
                self.set_configuration(sitemap_xml_context.configuration)
                self.set_lastmod(sitemap_xml_context.lastmod)
                self.set_objects(sitemap_xml_context.objects)
                self.set_objects_list_page_numbers(sitemap_xml_context.objects_list_page_numbers)
            elif isinstance(sitemap_xml_context, dict):
                for key, value in sitemap_xml_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(sitemap_xml_context)
            return self

        @configuration.setter
        def configuration(self, configuration):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            self.set_configuration(configuration)

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

        @objects_list_page_numbers.setter
        def objects_list_page_numbers(self, objects_list_page_numbers):
            '''
            :type objects_list_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            self.set_objects_list_page_numbers(objects_list_page_numbers)

    class FieldMetadata(object):
        CONFIGURATION = None
        LASTMOD = None
        OBJECTS = None
        OBJECTS_LIST_PAGE_NUMBERS = None

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
            return (cls.CONFIGURATION, cls.LASTMOD, cls.OBJECTS, cls.OBJECTS_LIST_PAGE_NUMBERS,)

    FieldMetadata.CONFIGURATION = FieldMetadata('configuration', pastpy.gen.site.site_configuration.SiteConfiguration, None)
    FieldMetadata.LASTMOD = FieldMetadata('lastmod', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.OBJECTS_LIST_PAGE_NUMBERS = FieldMetadata('objects_list_page_numbers', tuple, None)

    def __init__(
        self,
        configuration,
        lastmod,
        objects,
        objects_list_page_numbers,
    ):
        '''
        :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
        :type lastmod: str
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type objects_list_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
        '''

        if configuration is None:
            raise ValueError('configuration is required')
        if not isinstance(configuration, pastpy.gen.site.site_configuration.SiteConfiguration):
            raise TypeError("expected configuration to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(configuration))
        self.__configuration = configuration

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

        if objects_list_page_numbers is None:
            raise ValueError('objects_list_page_numbers is required')
        if not (isinstance(objects_list_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber), objects_list_page_numbers))) == 0):
            raise TypeError("expected objects_list_page_numbers to be a tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber) but it is a %s" % builtins.type(objects_list_page_numbers))
        self.__objects_list_page_numbers = objects_list_page_numbers

    def __eq__(self, other):
        if self.configuration != other.configuration:
            return False
        if self.lastmod != other.lastmod:
            return False
        if self.objects != other.objects:
            return False
        if self.objects_list_page_numbers != other.objects_list_page_numbers:
            return False
        return True

    def __hash__(self):
        return hash((self.configuration, self.lastmod, self.objects, self.objects_list_page_numbers,))

    def __iter__(self):
        return iter((self.configuration, self.lastmod, self.objects, self.objects_list_page_numbers,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('lastmod=' + "'" + self.lastmod.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('objects_list_page_numbers=' + repr(self.objects_list_page_numbers))
        return 'SitemapXmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('lastmod=' + "'" + self.lastmod.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('objects_list_page_numbers=' + repr(self.objects_list_page_numbers))
        return 'SitemapXmlContext(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def configuration(self):
        '''
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        return self.__configuration

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        configuration = _dict.get("configuration")
        if configuration is None:
            raise KeyError("configuration")
        configuration = pastpy.gen.site.site_configuration.SiteConfiguration.from_builtins(configuration)
        __builder.configuration = configuration

        lastmod = _dict.get("lastmod")
        if lastmod is None:
            raise KeyError("lastmod")
        __builder.lastmod = lastmod

        objects = _dict.get("objects")
        if objects is None:
            raise KeyError("objects")
        objects = tuple(pastpy.gen.site.site_object.SiteObject.from_builtins(element0) for element0 in objects)
        __builder.objects = objects

        objects_list_page_numbers = _dict.get("objects_list_page_numbers")
        if objects_list_page_numbers is None:
            raise KeyError("objects_list_page_numbers")
        objects_list_page_numbers = tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.from_builtins(element0) for element0 in objects_list_page_numbers)
        __builder.objects_list_page_numbers = objects_list_page_numbers

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
    def objects_list_page_numbers(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
        '''

        return self.__objects_list_page_numbers

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.sitemap_xml_context.SitemapXmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'configuration':
                init_kwds['configuration'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            elif ifield_name == 'lastmod':
                init_kwds['lastmod'] = iprot.read_string()
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'objects_list_page_numbers':
                init_kwds['objects_list_page_numbers'] = tuple([pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["configuration"] = self.configuration.to_builtins()
        dict_["lastmod"] = self.lastmod
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["objects_list_page_numbers"] = tuple(element0.to_builtins() for element0 in self.objects_list_page_numbers)
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.sitemap_xml_context.SitemapXmlContext
        '''

        oprot.write_struct_begin('SitemapXmlContext')

        oprot.write_field_begin(name='configuration', type=12, id=None)
        self.configuration.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='lastmod', type=11, id=None)
        oprot.write_string(self.lastmod)
        oprot.write_field_end()

        oprot.write_field_begin(name='objects', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects))
        for _0 in self.objects:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='objects_list_page_numbers', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects_list_page_numbers))
        for _0 in self.objects_list_page_numbers:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
