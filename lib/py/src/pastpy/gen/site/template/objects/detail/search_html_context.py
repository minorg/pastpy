import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_configuration
import pastpy.gen.site.template.footer_html_context
import pastpy.gen.site.template.navbar_html_context


class SearchHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            configuration=None,
            footer=None,
            navbar=None,
            object_card_html_mustache=None,
            root_relative_href=None,
        ):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type object_card_html_mustache: str
            :type root_relative_href: str
            '''

            self.__configuration = configuration
            self.__footer = footer
            self.__navbar = navbar
            self.__object_card_html_mustache = object_card_html_mustache
            self.__root_relative_href = root_relative_href

        def build(self):
            return SearchHtmlContext(configuration=self.__configuration, footer=self.__footer, navbar=self.__navbar, object_card_html_mustache=self.__object_card_html_mustache, root_relative_href=self.__root_relative_href)

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
            :type template: pastpy.gen.site.template.objects.detail.search_html_context.SearchHtmlContext
            :rtype: pastpy.gen.site.template.objects.detail.search_html_context.SearchHtmlContext
            '''

            builder = cls()
            builder.configuration = template.configuration
            builder.footer = template.footer
            builder.navbar = template.navbar
            builder.object_card_html_mustache = template.object_card_html_mustache
            builder.root_relative_href = template.root_relative_href
            return builder

        @property
        def navbar(self):
            '''
            :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            return self.__navbar

        @property
        def object_card_html_mustache(self):
            '''
            :rtype: str
            '''

            return self.__object_card_html_mustache

        @property
        def root_relative_href(self):
            '''
            :rtype: str
            '''

            return self.__root_relative_href

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

        def set_object_card_html_mustache(self, object_card_html_mustache):
            '''
            :type object_card_html_mustache: str
            '''

            if object_card_html_mustache is None:
                raise ValueError('object_card_html_mustache is required')
            if not isinstance(object_card_html_mustache, str):
                raise TypeError("expected object_card_html_mustache to be a str but it is a %s" % builtins.type(object_card_html_mustache))
            self.__object_card_html_mustache = object_card_html_mustache
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

        def update(self, search_html_context):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type object_card_html_mustache: str
            :type root_relative_href: str
            '''

            if isinstance(search_html_context, SearchHtmlContext):
                self.set_configuration(search_html_context.configuration)
                self.set_footer(search_html_context.footer)
                self.set_navbar(search_html_context.navbar)
                self.set_object_card_html_mustache(search_html_context.object_card_html_mustache)
                self.set_root_relative_href(search_html_context.root_relative_href)
            elif isinstance(search_html_context, dict):
                for key, value in search_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(search_html_context)
            return self

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

        @object_card_html_mustache.setter
        def object_card_html_mustache(self, object_card_html_mustache):
            '''
            :type object_card_html_mustache: str
            '''

            self.set_object_card_html_mustache(object_card_html_mustache)

        @root_relative_href.setter
        def root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            self.set_root_relative_href(root_relative_href)

    class FieldMetadata(object):
        CONFIGURATION = None
        FOOTER = None
        NAVBAR = None
        OBJECT_CARD_HTML_MUSTACHE = None
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
            return (cls.CONFIGURATION, cls.FOOTER, cls.NAVBAR, cls.OBJECT_CARD_HTML_MUSTACHE, cls.ROOT_RELATIVE_HREF,)

    FieldMetadata.CONFIGURATION = FieldMetadata('configuration', pastpy.gen.site.site_configuration.SiteConfiguration, None)
    FieldMetadata.FOOTER = FieldMetadata('footer', pastpy.gen.site.template.footer_html_context.FooterHtmlContext, None)
    FieldMetadata.NAVBAR = FieldMetadata('navbar', pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext, None)
    FieldMetadata.OBJECT_CARD_HTML_MUSTACHE = FieldMetadata('object_card_html_mustache', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.ROOT_RELATIVE_HREF = FieldMetadata('root_relative_href', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        configuration,
        footer,
        navbar,
        object_card_html_mustache,
        root_relative_href,
    ):
        '''
        :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
        :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        :type object_card_html_mustache: str
        :type root_relative_href: str
        '''

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

        if object_card_html_mustache is None:
            raise ValueError('object_card_html_mustache is required')
        if not isinstance(object_card_html_mustache, str):
            raise TypeError("expected object_card_html_mustache to be a str but it is a %s" % builtins.type(object_card_html_mustache))
        self.__object_card_html_mustache = object_card_html_mustache

        if root_relative_href is None:
            raise ValueError('root_relative_href is required')
        if not isinstance(root_relative_href, str):
            raise TypeError("expected root_relative_href to be a str but it is a %s" % builtins.type(root_relative_href))
        self.__root_relative_href = root_relative_href

    def __eq__(self, other):
        if self.configuration != other.configuration:
            return False
        if self.footer != other.footer:
            return False
        if self.navbar != other.navbar:
            return False
        if self.object_card_html_mustache != other.object_card_html_mustache:
            return False
        if self.root_relative_href != other.root_relative_href:
            return False
        return True

    def __hash__(self):
        return hash((self.configuration, self.footer, self.navbar, self.object_card_html_mustache, self.root_relative_href,))

    def __iter__(self):
        return iter((self.configuration, self.footer, self.navbar, self.object_card_html_mustache, self.root_relative_href,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('object_card_html_mustache=' + "'" + self.object_card_html_mustache.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SearchHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('object_card_html_mustache=' + "'" + self.object_card_html_mustache.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SearchHtmlContext(' + ', '.join(field_reprs) + ')'

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

        object_card_html_mustache = _dict.get("object_card_html_mustache")
        if object_card_html_mustache is None:
            raise KeyError("object_card_html_mustache")
        __builder.object_card_html_mustache = object_card_html_mustache

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
    def object_card_html_mustache(self):
        '''
        :rtype: str
        '''

        return self.__object_card_html_mustache

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.search_html_context.SearchHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'configuration':
                init_kwds['configuration'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            elif ifield_name == 'footer':
                init_kwds['footer'] = pastpy.gen.site.template.footer_html_context.FooterHtmlContext.read(iprot)
            elif ifield_name == 'navbar':
                init_kwds['navbar'] = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.read(iprot)
            elif ifield_name == 'object_card_html_mustache':
                init_kwds['object_card_html_mustache'] = iprot.read_string()
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
        dict_["configuration"] = self.configuration.to_builtins()
        dict_["footer"] = self.footer.to_builtins()
        dict_["navbar"] = self.navbar.to_builtins()
        dict_["object_card_html_mustache"] = self.object_card_html_mustache
        dict_["root_relative_href"] = self.root_relative_href
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.search_html_context.SearchHtmlContext
        '''

        oprot.write_struct_begin('SearchHtmlContext')

        oprot.write_field_begin(name='configuration', type=12, id=None)
        self.configuration.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='footer', type=12, id=None)
        self.footer.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='navbar', type=12, id=None)
        self.navbar.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='object_card_html_mustache', type=11, id=None)
        oprot.write_string(self.object_card_html_mustache)
        oprot.write_field_end()

        oprot.write_field_begin(name='root_relative_href', type=11, id=None)
        oprot.write_string(self.root_relative_href)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
