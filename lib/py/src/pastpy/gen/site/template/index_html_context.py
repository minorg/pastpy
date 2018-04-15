import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_configuration
import pastpy.gen.site.template.footer_html_context
import pastpy.gen.site.template.navbar_html_context


class IndexHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            configuration=None,
            footer=None,
            has_featured_searches=None,
            navbar=None,
            root_relative_href=None,
        ):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type has_featured_searches: bool
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type root_relative_href: str
            '''

            self.__configuration = configuration
            self.__footer = footer
            self.__has_featured_searches = has_featured_searches
            self.__navbar = navbar
            self.__root_relative_href = root_relative_href

        def build(self):
            return IndexHtmlContext(configuration=self.__configuration, footer=self.__footer, has_featured_searches=self.__has_featured_searches, navbar=self.__navbar, root_relative_href=self.__root_relative_href)

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
            :type template: pastpy.gen.site.template.index_html_context.IndexHtmlContext
            :rtype: pastpy.gen.site.template.index_html_context.IndexHtmlContext
            '''

            builder = cls()
            builder.configuration = template.configuration
            builder.footer = template.footer
            builder.has_featured_searches = template.has_featured_searches
            builder.navbar = template.navbar
            builder.root_relative_href = template.root_relative_href
            return builder

        @property
        def has_featured_searches(self):
            '''
            :rtype: bool
            '''

            return self.__has_featured_searches

        @property
        def navbar(self):
            '''
            :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            return self.__navbar

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

        def update(self, index_html_context):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type has_featured_searches: bool
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type root_relative_href: str
            '''

            if isinstance(index_html_context, IndexHtmlContext):
                self.set_configuration(index_html_context.configuration)
                self.set_footer(index_html_context.footer)
                self.set_has_featured_searches(index_html_context.has_featured_searches)
                self.set_navbar(index_html_context.navbar)
                self.set_root_relative_href(index_html_context.root_relative_href)
            elif isinstance(index_html_context, dict):
                for key, value in index_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(index_html_context)
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

        @has_featured_searches.setter
        def has_featured_searches(self, has_featured_searches):
            '''
            :type has_featured_searches: bool
            '''

            self.set_has_featured_searches(has_featured_searches)

        @navbar.setter
        def navbar(self, navbar):
            '''
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            self.set_navbar(navbar)

        @root_relative_href.setter
        def root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            self.set_root_relative_href(root_relative_href)

    class FieldMetadata(object):
        CONFIGURATION = None
        FOOTER = None
        HAS_FEATURED_SEARCHES = None
        NAVBAR = None
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
            return (cls.CONFIGURATION, cls.FOOTER, cls.HAS_FEATURED_SEARCHES, cls.NAVBAR, cls.ROOT_RELATIVE_HREF,)

    FieldMetadata.CONFIGURATION = FieldMetadata('configuration', pastpy.gen.site.site_configuration.SiteConfiguration, None)
    FieldMetadata.FOOTER = FieldMetadata('footer', pastpy.gen.site.template.footer_html_context.FooterHtmlContext, None)
    FieldMetadata.HAS_FEATURED_SEARCHES = FieldMetadata('has_featured_searches', bool, None)
    FieldMetadata.NAVBAR = FieldMetadata('navbar', pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext, None)
    FieldMetadata.ROOT_RELATIVE_HREF = FieldMetadata('root_relative_href', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        configuration,
        footer,
        has_featured_searches,
        navbar,
        root_relative_href,
    ):
        '''
        :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
        :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        :type has_featured_searches: bool
        :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
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

        if has_featured_searches is None:
            raise ValueError('has_featured_searches is required')
        if not isinstance(has_featured_searches, bool):
            raise TypeError("expected has_featured_searches to be a bool but it is a %s" % builtins.type(has_featured_searches))
        self.__has_featured_searches = has_featured_searches

        if navbar is None:
            raise ValueError('navbar is required')
        if not isinstance(navbar, pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext):
            raise TypeError("expected navbar to be a pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext but it is a %s" % builtins.type(navbar))
        self.__navbar = navbar

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
        if self.has_featured_searches != other.has_featured_searches:
            return False
        if self.navbar != other.navbar:
            return False
        if self.root_relative_href != other.root_relative_href:
            return False
        return True

    def __hash__(self):
        return hash((self.configuration, self.footer, self.has_featured_searches, self.navbar, self.root_relative_href,))

    def __iter__(self):
        return iter((self.configuration, self.footer, self.has_featured_searches, self.navbar, self.root_relative_href,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('has_featured_searches=' + repr(self.has_featured_searches))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'IndexHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('has_featured_searches=' + repr(self.has_featured_searches))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'IndexHtmlContext(' + ', '.join(field_reprs) + ')'

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

        has_featured_searches = _dict.get("has_featured_searches")
        if has_featured_searches is None:
            raise KeyError("has_featured_searches")
        __builder.has_featured_searches = has_featured_searches

        navbar = _dict.get("navbar")
        if navbar is None:
            raise KeyError("navbar")
        navbar = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.from_builtins(navbar)
        __builder.navbar = navbar

        root_relative_href = _dict.get("root_relative_href")
        if root_relative_href is None:
            raise KeyError("root_relative_href")
        __builder.root_relative_href = root_relative_href

        return __builder.build()

    @property
    def has_featured_searches(self):
        '''
        :rtype: bool
        '''

        return self.__has_featured_searches

    @property
    def navbar(self):
        '''
        :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        '''

        return self.__navbar

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
            elif ifield_name == 'configuration':
                init_kwds['configuration'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            elif ifield_name == 'footer':
                init_kwds['footer'] = pastpy.gen.site.template.footer_html_context.FooterHtmlContext.read(iprot)
            elif ifield_name == 'has_featured_searches':
                init_kwds['has_featured_searches'] = iprot.read_bool()
            elif ifield_name == 'navbar':
                init_kwds['navbar'] = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.read(iprot)
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
        dict_["has_featured_searches"] = self.has_featured_searches
        dict_["navbar"] = self.navbar.to_builtins()
        dict_["root_relative_href"] = self.root_relative_href
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.index_html_context.IndexHtmlContext
        '''

        oprot.write_struct_begin('IndexHtmlContext')

        oprot.write_field_begin(name='configuration', type=12, id=None)
        self.configuration.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='footer', type=12, id=None)
        self.footer.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='has_featured_searches', type=2, id=None)
        oprot.write_bool(self.has_featured_searches)
        oprot.write_field_end()

        oprot.write_field_begin(name='navbar', type=12, id=None)
        self.navbar.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='root_relative_href', type=11, id=None)
        oprot.write_string(self.root_relative_href)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
