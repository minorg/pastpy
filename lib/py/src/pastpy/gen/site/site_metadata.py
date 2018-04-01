import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_configuration
import pastpy.gen.site.site_nav_items


class SiteMetadata(object):
    class Builder(object):
        def __init__(
            self,
            configuration=None,
            current_year=None,
            nav_items=None,
            root_relative_href=None,
        ):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type current_year: int
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            :type root_relative_href: str
            '''

            self.__configuration = configuration
            self.__current_year = current_year
            self.__nav_items = nav_items
            self.__root_relative_href = root_relative_href

        def build(self):
            return SiteMetadata(configuration=self.__configuration, current_year=self.__current_year, nav_items=self.__nav_items, root_relative_href=self.__root_relative_href)

        @property
        def configuration(self):
            '''
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            return self.__configuration

        @property
        def current_year(self):
            '''
            :rtype: int
            '''

            return self.__current_year

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_metadata.SiteMetadata
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            builder = cls()
            builder.configuration = template.configuration
            builder.current_year = template.current_year
            builder.nav_items = template.nav_items
            builder.root_relative_href = template.root_relative_href
            return builder

        @property
        def nav_items(self):
            '''
            :rtype: pastpy.gen.site.site_nav_items.SiteNavItems
            '''

            return self.__nav_items

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

        def set_current_year(self, current_year):
            '''
            :type current_year: int
            '''

            if current_year is None:
                raise ValueError('current_year is required')
            if not isinstance(current_year, int):
                raise TypeError("expected current_year to be a int but it is a %s" % builtins.type(current_year))
            self.__current_year = current_year
            return self

        def set_nav_items(self, nav_items):
            '''
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            '''

            if nav_items is None:
                raise ValueError('nav_items is required')
            if not isinstance(nav_items, pastpy.gen.site.site_nav_items.SiteNavItems):
                raise TypeError("expected nav_items to be a pastpy.gen.site.site_nav_items.SiteNavItems but it is a %s" % builtins.type(nav_items))
            self.__nav_items = nav_items
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

        def update(self, site_metadata):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            :type current_year: int
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            :type root_relative_href: str
            '''

            if isinstance(site_metadata, SiteMetadata):
                self.set_configuration(site_metadata.configuration)
                self.set_current_year(site_metadata.current_year)
                self.set_nav_items(site_metadata.nav_items)
                self.set_root_relative_href(site_metadata.root_relative_href)
            elif isinstance(site_metadata, dict):
                for key, value in site_metadata.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_metadata)
            return self

        @configuration.setter
        def configuration(self, configuration):
            '''
            :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            self.set_configuration(configuration)

        @current_year.setter
        def current_year(self, current_year):
            '''
            :type current_year: int
            '''

            self.set_current_year(current_year)

        @nav_items.setter
        def nav_items(self, nav_items):
            '''
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            '''

            self.set_nav_items(nav_items)

        @root_relative_href.setter
        def root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            self.set_root_relative_href(root_relative_href)

    class FieldMetadata(object):
        CONFIGURATION = None
        CURRENT_YEAR = None
        NAV_ITEMS = None
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
            return (cls.CONFIGURATION, cls.CURRENT_YEAR, cls.NAV_ITEMS, cls.ROOT_RELATIVE_HREF,)

    FieldMetadata.CONFIGURATION = FieldMetadata('configuration', pastpy.gen.site.site_configuration.SiteConfiguration, None)
    FieldMetadata.CURRENT_YEAR = FieldMetadata('current_year', int, None)
    FieldMetadata.NAV_ITEMS = FieldMetadata('nav_items', pastpy.gen.site.site_nav_items.SiteNavItems, None)
    FieldMetadata.ROOT_RELATIVE_HREF = FieldMetadata('root_relative_href', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        configuration,
        current_year,
        nav_items,
        root_relative_href,
    ):
        '''
        :type configuration: pastpy.gen.site.site_configuration.SiteConfiguration
        :type current_year: int
        :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
        :type root_relative_href: str
        '''

        if configuration is None:
            raise ValueError('configuration is required')
        if not isinstance(configuration, pastpy.gen.site.site_configuration.SiteConfiguration):
            raise TypeError("expected configuration to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(configuration))
        self.__configuration = configuration

        if current_year is None:
            raise ValueError('current_year is required')
        if not isinstance(current_year, int):
            raise TypeError("expected current_year to be a int but it is a %s" % builtins.type(current_year))
        self.__current_year = current_year

        if nav_items is None:
            raise ValueError('nav_items is required')
        if not isinstance(nav_items, pastpy.gen.site.site_nav_items.SiteNavItems):
            raise TypeError("expected nav_items to be a pastpy.gen.site.site_nav_items.SiteNavItems but it is a %s" % builtins.type(nav_items))
        self.__nav_items = nav_items

        if root_relative_href is None:
            raise ValueError('root_relative_href is required')
        if not isinstance(root_relative_href, str):
            raise TypeError("expected root_relative_href to be a str but it is a %s" % builtins.type(root_relative_href))
        self.__root_relative_href = root_relative_href

    def __eq__(self, other):
        if self.configuration != other.configuration:
            return False
        if self.current_year != other.current_year:
            return False
        if self.nav_items != other.nav_items:
            return False
        if self.root_relative_href != other.root_relative_href:
            return False
        return True

    def __hash__(self):
        return hash((self.configuration, self.current_year, self.nav_items, self.root_relative_href,))

    def __iter__(self):
        return iter((self.configuration, self.current_year, self.nav_items, self.root_relative_href,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('current_year=' + repr(self.current_year))
        field_reprs.append('nav_items=' + repr(self.nav_items))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteMetadata(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('configuration=' + repr(self.configuration))
        field_reprs.append('current_year=' + repr(self.current_year))
        field_reprs.append('nav_items=' + repr(self.nav_items))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteMetadata(' + ', '.join(field_reprs) + ')'

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
    def current_year(self):
        '''
        :rtype: int
        '''

        return self.__current_year

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

        current_year = _dict.get("current_year")
        if current_year is None:
            raise KeyError("current_year")
        __builder.current_year = current_year

        nav_items = _dict.get("nav_items")
        if nav_items is None:
            raise KeyError("nav_items")
        nav_items = pastpy.gen.site.site_nav_items.SiteNavItems.from_builtins(nav_items)
        __builder.nav_items = nav_items

        root_relative_href = _dict.get("root_relative_href")
        if root_relative_href is None:
            raise KeyError("root_relative_href")
        __builder.root_relative_href = root_relative_href

        return __builder.build()

    @property
    def nav_items(self):
        '''
        :rtype: pastpy.gen.site.site_nav_items.SiteNavItems
        '''

        return self.__nav_items

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'configuration':
                init_kwds['configuration'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            elif ifield_name == 'current_year':
                init_kwds['current_year'] = iprot.read_i32()
            elif ifield_name == 'nav_items':
                init_kwds['nav_items'] = pastpy.gen.site.site_nav_items.SiteNavItems.read(iprot)
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
        dict_["current_year"] = self.current_year
        dict_["nav_items"] = self.nav_items.to_builtins()
        dict_["root_relative_href"] = self.root_relative_href
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        oprot.write_struct_begin('SiteMetadata')

        oprot.write_field_begin(name='configuration', type=12, id=None)
        self.configuration.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='current_year', type=8, id=None)
        oprot.write_i32(self.current_year)
        oprot.write_field_end()

        oprot.write_field_begin(name='nav_items', type=12, id=None)
        self.nav_items.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='root_relative_href', type=11, id=None)
        oprot.write_string(self.root_relative_href)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
