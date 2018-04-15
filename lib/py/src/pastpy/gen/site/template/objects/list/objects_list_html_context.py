from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_configuration
import pastpy.gen.site.site_object
import pastpy.gen.site.site_pagination
import pastpy.gen.site.template.footer_html_context
import pastpy.gen.site.template.navbar_html_context


class ObjectsListHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            absolute_href=None,
            configuration=None,
            footer=None,
            navbar=None,
            objects=None,
            pagination=None,
            root_relative_href=None,
        ):
            '''
            :type absolute_href: str
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            :type root_relative_href: str
            '''

            self.__absolute_href = absolute_href
            self.__configuration = configuration
            self.__footer = footer
            self.__navbar = navbar
            self.__objects = objects
            self.__pagination = pagination
            self.__root_relative_href = root_relative_href

        def build(self):
            return ObjectsListHtmlContext(absolute_href=self.__absolute_href, configuration=self.__configuration, footer=self.__footer, navbar=self.__navbar, objects=self.__objects, pagination=self.__pagination, root_relative_href=self.__root_relative_href)

        @property
        def absolute_href(self):
            '''
            :rtype: str
            '''

            return self.__absolute_href

        @property
        def configuration(self):
            '''
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            return self.__configuration

        @property
        def footer(self):
            '''
            :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            '''

            return self.__footer

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.objects.list.objects_list_html_context.ObjectsListHtmlContext
            :rtype: pastpy.gen.site.template.objects.list.objects_list_html_context.ObjectsListHtmlContext
            '''

            builder = cls()
            builder.absolute_href = template.absolute_href
            builder.configuration = template.configuration
            builder.footer = template.footer
            builder.navbar = template.navbar
            builder.objects = template.objects
            builder.pagination = template.pagination
            builder.root_relative_href = template.root_relative_href
            return builder

        @property
        def navbar(self):
            '''
            :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            return self.__navbar

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

        @property
        def root_relative_href(self):
            '''
            :rtype: str
            '''

            return self.__root_relative_href

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

        def set_footer(self, footer):
            '''
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            '''

            if footer is None:
                raise ValueError('footer is required')
            if not isinstance(footer, pastpy.gen.site.template.footer_html_context.FooterHtmlContext):
                raise TypeError("expected footer to be a pastpy.gen.site.template.footer_html_context.FooterHtmlContext but it is a %s" % builtins.type(footer))
            self.__footer = footer
            return self

        def set_navbar(self, navbar):
            '''
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            if navbar is None:
                raise ValueError('navbar is required')
            if not isinstance(navbar, pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext):
                raise TypeError("expected navbar to be a pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext but it is a %s" % builtins.type(navbar))
            self.__navbar = navbar
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

        def set_root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            if root_relative_href is None:
                raise ValueError('root_relative_href is required')
            if not isinstance(root_relative_href, str):
                raise TypeError("expected root_relative_href to be a str but it is a %s" % builtins.type(root_relative_href))
            self.__root_relative_href = root_relative_href
            return self

        def update(self, objects_list_html_context):
            '''
            :type absolute_href: str
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type pagination: pastpy.gen.site.site_pagination.SitePagination
            :type root_relative_href: str
            '''

            if isinstance(objects_list_html_context, ObjectsListHtmlContext):
                self.set_absolute_href(objects_list_html_context.absolute_href)
                self.set_configuration(objects_list_html_context.configuration)
                self.set_footer(objects_list_html_context.footer)
                self.set_navbar(objects_list_html_context.navbar)
                self.set_objects(objects_list_html_context.objects)
                self.set_pagination(objects_list_html_context.pagination)
                self.set_root_relative_href(objects_list_html_context.root_relative_href)
            elif isinstance(objects_list_html_context, dict):
                for key, value in objects_list_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(objects_list_html_context)
            return self

        @absolute_href.setter
        def absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            self.set_absolute_href(absolute_href)

        @configuration.setter
        def configuration(self, configuration):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            self.set_configuration(configuration)

        @footer.setter
        def footer(self, footer):
            '''
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            '''

            self.set_footer(footer)

        @navbar.setter
        def navbar(self, navbar):
            '''
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            self.set_navbar(navbar)

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

        @root_relative_href.setter
        def root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            self.set_root_relative_href(root_relative_href)

    class FieldMetadata(object):
        ABSOLUTE_HREF = None
        CONFIGURATION = None
        FOOTER = None
        NAVBAR = None
        OBJECTS = None
        PAGINATION = None
        ROOT_RELATIVE_HREF = None

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
            return (cls.ABSOLUTE_HREF, cls.CONFIGURATION, cls.FOOTER, cls.NAVBAR, cls.OBJECTS, cls.PAGINATION, cls.ROOT_RELATIVE_HREF,)

    FieldMetadata.ABSOLUTE_HREF = FieldMetadata('absolute_href', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.CONFIGURATION = FieldMetadata('configuration', pastpy.gen.site.site_configuration.SiteConfiguration, None)
    FieldMetadata.FOOTER = FieldMetadata('footer', pastpy.gen.site.template.footer_html_context.FooterHtmlContext, None)
    FieldMetadata.NAVBAR = FieldMetadata('navbar', pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.PAGINATION = FieldMetadata('pagination', pastpy.gen.site.site_pagination.SitePagination, None)
    FieldMetadata.ROOT_RELATIVE_HREF = FieldMetadata('root_relative_href', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        absolute_href,
        configuration,
        footer,
        navbar,
        objects,
        pagination,
        root_relative_href,
    ):
        '''
        :type absolute_href: str
        :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
        :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type pagination: pastpy.gen.site.site_pagination.SitePagination
        :type root_relative_href: str
        '''

        if absolute_href is None:
            raise ValueError('absolute_href is required')
        if not isinstance(absolute_href, str):
            raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
        self.__absolute_href = absolute_href

        if configuration is None:
            raise ValueError('configuration is required')
        if not isinstance(configuration, pastpy.gen.site.site_configuration.SiteConfiguration):
            raise TypeError("expected configuration to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(configuration))
        self.__configuration = configuration

        if footer is None:
            raise ValueError('footer is required')
        if not isinstance(footer, pastpy.gen.site.template.footer_html_context.FooterHtmlContext):
            raise TypeError("expected footer to be a pastpy.gen.site.template.footer_html_context.FooterHtmlContext but it is a %s" % builtins.type(footer))
        self.__footer = footer

        if navbar is None:
            raise ValueError('navbar is required')
        if not isinstance(navbar, pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext):
            raise TypeError("expected navbar to be a pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext but it is a %s" % builtins.type(navbar))
        self.__navbar = navbar

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

        if root_relative_href is None:
            raise ValueError('root_relative_href is required')
        if not isinstance(root_relative_href, str):
            raise TypeError("expected root_relative_href to be a str but it is a %s" % builtins.type(root_relative_href))
        self.__root_relative_href = root_relative_href

    def __eq__(self, other):
        if self.absolute_href != other.absolute_href:
            return False
        if self.configuration != other.configuration:
            return False
        if self.footer != other.footer:
            return False
        if self.navbar != other.navbar:
            return False
        if self.objects != other.objects:
            return False
        if self.pagination != other.pagination:
            return False
        if self.root_relative_href != other.root_relative_href:
            return False
        return True

    def __hash__(self):
        return hash((self.absolute_href, self.configuration, self.footer, self.navbar, self.objects, self.pagination, self.root_relative_href,))

    def __iter__(self):
        return iter((self.absolute_href, self.configuration, self.footer, self.navbar, self.objects, self.pagination, self.root_relative_href,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('pagination=' + repr(self.pagination))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectsListHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('pagination=' + repr(self.pagination))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectsListHtmlContext(' + ', '.join(field_reprs) + ')'

    @property
    def absolute_href(self):
        '''
        :rtype: str
        '''

        return self.__absolute_href

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def configuration(self):
        '''
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        return self.__configuration

    @property
    def footer(self):
        '''
        :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        '''

        return self.__footer

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        absolute_href = _dict.get("absolute_href")
        if absolute_href is None:
            raise KeyError("absolute_href")
        __builder.absolute_href = absolute_href

        configuration = _dict.get("configuration")
        if configuration is None:
            raise KeyError("configuration")
        configuration = pastpy.gen.site.site_configuration.SiteConfiguration.from_builtins(configuration)
        __builder.configuration = configuration

        footer = _dict.get("footer")
        if footer is None:
            raise KeyError("footer")
        footer = pastpy.gen.site.template.footer_html_context.FooterHtmlContext.from_builtins(footer)
        __builder.footer = footer

        navbar = _dict.get("navbar")
        if navbar is None:
            raise KeyError("navbar")
        navbar = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.from_builtins(navbar)
        __builder.navbar = navbar

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

        root_relative_href = _dict.get("root_relative_href")
        if root_relative_href is None:
            raise KeyError("root_relative_href")
        __builder.root_relative_href = root_relative_href

        return __builder.build()

    @property
    def navbar(self):
        '''
        :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        '''

        return self.__navbar

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
        :rtype: pastpy.gen.site.template.objects.list.objects_list_html_context.ObjectsListHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'absolute_href':
                init_kwds['absolute_href'] = iprot.read_string()
            elif ifield_name == 'configuration':
                init_kwds['configuration'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            elif ifield_name == 'footer':
                init_kwds['footer'] = pastpy.gen.site.template.footer_html_context.FooterHtmlContext.read(iprot)
            elif ifield_name == 'navbar':
                init_kwds['navbar'] = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.read(iprot)
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'pagination':
                init_kwds['pagination'] = pastpy.gen.site.site_pagination.SitePagination.read(iprot)
            elif ifield_name == 'root_relative_href':
                init_kwds['root_relative_href'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def root_relative_href(self):
        '''
        :rtype: str
        '''

        return self.__root_relative_href

    def to_builtins(self):
        dict_ = {}
        dict_["absolute_href"] = self.absolute_href
        dict_["configuration"] = self.configuration.to_builtins()
        dict_["footer"] = self.footer.to_builtins()
        dict_["navbar"] = self.navbar.to_builtins()
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["pagination"] = self.pagination.to_builtins()
        dict_["root_relative_href"] = self.root_relative_href
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.objects.list.objects_list_html_context.ObjectsListHtmlContext
        '''

        oprot.write_struct_begin('ObjectsListHtmlContext')

        oprot.write_field_begin(name='absolute_href', type=11, id=None)
        oprot.write_string(self.absolute_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='configuration', type=12, id=None)
        self.configuration.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='footer', type=12, id=None)
        self.footer.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='navbar', type=12, id=None)
        self.navbar.write(oprot)
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

        oprot.write_field_begin(name='root_relative_href', type=11, id=None)
        oprot.write_string(self.root_relative_href)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
