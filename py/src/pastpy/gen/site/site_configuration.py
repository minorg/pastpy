from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_featured_search


class SiteConfiguration(object):
    class Builder(object):
        def __init__(
            self,
            base_url=None,
            copyright_holder="Your Collection",
            name="Your Collection",
            output_dir_path="site",
            featured_searches=None,
            institution_name=None,
            template_dir_path=None,
            theme_css_file_path=None,
        ):
            '''
            :type base_url: str
            :type copyright_holder: str
            :type name: str
            :type output_dir_path: str
            :type featured_searches: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) or None
            :type institution_name: str or None
            :type template_dir_path: str or None
            :type theme_css_file_path: str or None
            '''

            self.__base_url = base_url
            self.__copyright_holder = copyright_holder
            self.__name = name
            self.__output_dir_path = output_dir_path
            self.__featured_searches = featured_searches
            self.__institution_name = institution_name
            self.__template_dir_path = template_dir_path
            self.__theme_css_file_path = theme_css_file_path

        def build(self):
            return SiteConfiguration(base_url=self.__base_url, copyright_holder=self.__copyright_holder, name=self.__name, output_dir_path=self.__output_dir_path, featured_searches=self.__featured_searches, institution_name=self.__institution_name, template_dir_path=self.__template_dir_path, theme_css_file_path=self.__theme_css_file_path)

        @property
        def base_url(self):
            '''
            :rtype: str
            '''

            return self.__base_url

        @property
        def copyright_holder(self):
            '''
            :rtype: str
            '''

            return self.__copyright_holder

        @property
        def featured_searches(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch)
            '''

            return self.__featured_searches

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_configuration.SiteConfiguration
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            builder = cls()
            builder.base_url = template.base_url
            builder.copyright_holder = template.copyright_holder
            builder.name = template.name
            builder.output_dir_path = template.output_dir_path
            builder.featured_searches = template.featured_searches
            builder.institution_name = template.institution_name
            builder.template_dir_path = template.template_dir_path
            builder.theme_css_file_path = template.theme_css_file_path
            return builder

        @property
        def institution_name(self):
            '''
            :rtype: str
            '''

            return self.__institution_name

        @property
        def name(self):
            '''
            :rtype: str
            '''

            return self.__name

        @property
        def output_dir_path(self):
            '''
            :rtype: str
            '''

            return self.__output_dir_path

        def set_base_url(self, base_url):
            '''
            :type base_url: str
            '''

            if base_url is None:
                raise ValueError('base_url is required')
            if not isinstance(base_url, str):
                raise TypeError("expected base_url to be a str but it is a %s" % builtins.type(base_url))
            self.__base_url = base_url
            return self

        def set_copyright_holder(self, copyright_holder):
            '''
            :type copyright_holder: str
            '''

            if copyright_holder is None:
                raise ValueError('copyright_holder is required')
            if not isinstance(copyright_holder, str):
                raise TypeError("expected copyright_holder to be a str but it is a %s" % builtins.type(copyright_holder))
            self.__copyright_holder = copyright_holder
            return self

        def set_featured_searches(self, featured_searches):
            '''
            :type featured_searches: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) or None
            '''

            if featured_searches is not None:
                if not (isinstance(featured_searches, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_featured_search.SiteFeaturedSearch), featured_searches))) == 0):
                    raise TypeError("expected featured_searches to be a tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) but it is a %s" % builtins.type(featured_searches))
            self.__featured_searches = featured_searches
            return self

        def set_institution_name(self, institution_name):
            '''
            :type institution_name: str or None
            '''

            if institution_name is not None:
                if not isinstance(institution_name, str):
                    raise TypeError("expected institution_name to be a str but it is a %s" % builtins.type(institution_name))
            self.__institution_name = institution_name
            return self

        def set_name(self, name):
            '''
            :type name: str
            '''

            if name is None:
                raise ValueError('name is required')
            if not isinstance(name, str):
                raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
            self.__name = name
            return self

        def set_output_dir_path(self, output_dir_path):
            '''
            :type output_dir_path: str
            '''

            if output_dir_path is None:
                raise ValueError('output_dir_path is required')
            if not isinstance(output_dir_path, str):
                raise TypeError("expected output_dir_path to be a str but it is a %s" % builtins.type(output_dir_path))
            self.__output_dir_path = output_dir_path
            return self

        def set_template_dir_path(self, template_dir_path):
            '''
            :type template_dir_path: str or None
            '''

            if template_dir_path is not None:
                if not isinstance(template_dir_path, str):
                    raise TypeError("expected template_dir_path to be a str but it is a %s" % builtins.type(template_dir_path))
            self.__template_dir_path = template_dir_path
            return self

        def set_theme_css_file_path(self, theme_css_file_path):
            '''
            :type theme_css_file_path: str or None
            '''

            if theme_css_file_path is not None:
                if not isinstance(theme_css_file_path, str):
                    raise TypeError("expected theme_css_file_path to be a str but it is a %s" % builtins.type(theme_css_file_path))
            self.__theme_css_file_path = theme_css_file_path
            return self

        @property
        def template_dir_path(self):
            '''
            :rtype: str
            '''

            return self.__template_dir_path

        @property
        def theme_css_file_path(self):
            '''
            :rtype: str
            '''

            return self.__theme_css_file_path

        def update(self, site_configuration):
            '''
            :type base_url: str
            :type copyright_holder: str
            :type name: str
            :type output_dir_path: str
            :type featured_searches: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) or None
            :type institution_name: str or None
            :type template_dir_path: str or None
            :type theme_css_file_path: str or None
            '''

            if isinstance(site_configuration, SiteConfiguration):
                self.set_base_url(site_configuration.base_url)
                self.set_copyright_holder(site_configuration.copyright_holder)
                self.set_name(site_configuration.name)
                self.set_output_dir_path(site_configuration.output_dir_path)
                self.set_featured_searches(site_configuration.featured_searches)
                self.set_institution_name(site_configuration.institution_name)
                self.set_template_dir_path(site_configuration.template_dir_path)
                self.set_theme_css_file_path(site_configuration.theme_css_file_path)
            elif isinstance(site_configuration, dict):
                for key, value in site_configuration.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_configuration)
            return self

        @base_url.setter
        def base_url(self, base_url):
            '''
            :type base_url: str
            '''

            self.set_base_url(base_url)

        @copyright_holder.setter
        def copyright_holder(self, copyright_holder):
            '''
            :type copyright_holder: str
            '''

            self.set_copyright_holder(copyright_holder)

        @featured_searches.setter
        def featured_searches(self, featured_searches):
            '''
            :type featured_searches: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) or None
            '''

            self.set_featured_searches(featured_searches)

        @institution_name.setter
        def institution_name(self, institution_name):
            '''
            :type institution_name: str or None
            '''

            self.set_institution_name(institution_name)

        @name.setter
        def name(self, name):
            '''
            :type name: str
            '''

            self.set_name(name)

        @output_dir_path.setter
        def output_dir_path(self, output_dir_path):
            '''
            :type output_dir_path: str
            '''

            self.set_output_dir_path(output_dir_path)

        @template_dir_path.setter
        def template_dir_path(self, template_dir_path):
            '''
            :type template_dir_path: str or None
            '''

            self.set_template_dir_path(template_dir_path)

        @theme_css_file_path.setter
        def theme_css_file_path(self, theme_css_file_path):
            '''
            :type theme_css_file_path: str or None
            '''

            self.set_theme_css_file_path(theme_css_file_path)

    class FieldMetadata(object):
        BASE_URL = None
        COPYRIGHT_HOLDER = None
        NAME = None
        OUTPUT_DIR_PATH = None
        FEATURED_SEARCHES = None
        INSTITUTION_NAME = None
        TEMPLATE_DIR_PATH = None
        THEME_CSS_FILE_PATH = None

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
            return (cls.BASE_URL, cls.COPYRIGHT_HOLDER, cls.NAME, cls.OUTPUT_DIR_PATH, cls.FEATURED_SEARCHES, cls.INSTITUTION_NAME, cls.TEMPLATE_DIR_PATH, cls.THEME_CSS_FILE_PATH,)

    FieldMetadata.BASE_URL = FieldMetadata('base_url', str, None)
    FieldMetadata.COPYRIGHT_HOLDER = FieldMetadata('copyright_holder', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.NAME = FieldMetadata('name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.OUTPUT_DIR_PATH = FieldMetadata('output_dir_path', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.FEATURED_SEARCHES = FieldMetadata('featured_searches', tuple, None)
    FieldMetadata.INSTITUTION_NAME = FieldMetadata('institution_name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.TEMPLATE_DIR_PATH = FieldMetadata('template_dir_path', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.THEME_CSS_FILE_PATH = FieldMetadata('theme_css_file_path', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        base_url,
        copyright_holder="Your Collection",
        name="Your Collection",
        output_dir_path="site",
        featured_searches=None,
        institution_name=None,
        template_dir_path=None,
        theme_css_file_path=None,
    ):
        '''
        :type base_url: str
        :type copyright_holder: str
        :type name: str
        :type output_dir_path: str
        :type featured_searches: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) or None
        :type institution_name: str or None
        :type template_dir_path: str or None
        :type theme_css_file_path: str or None
        '''

        if base_url is None:
            raise ValueError('base_url is required')
        if not isinstance(base_url, str):
            raise TypeError("expected base_url to be a str but it is a %s" % builtins.type(base_url))
        self.__base_url = base_url

        if copyright_holder is None:
            raise ValueError('copyright_holder is required')
        if not isinstance(copyright_holder, str):
            raise TypeError("expected copyright_holder to be a str but it is a %s" % builtins.type(copyright_holder))
        self.__copyright_holder = copyright_holder

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, str):
            raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
        self.__name = name

        if output_dir_path is None:
            raise ValueError('output_dir_path is required')
        if not isinstance(output_dir_path, str):
            raise TypeError("expected output_dir_path to be a str but it is a %s" % builtins.type(output_dir_path))
        self.__output_dir_path = output_dir_path

        if featured_searches is not None:
            if not (isinstance(featured_searches, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_featured_search.SiteFeaturedSearch), featured_searches))) == 0):
                raise TypeError("expected featured_searches to be a tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch) but it is a %s" % builtins.type(featured_searches))
        self.__featured_searches = featured_searches

        if institution_name is not None:
            if not isinstance(institution_name, str):
                raise TypeError("expected institution_name to be a str but it is a %s" % builtins.type(institution_name))
        self.__institution_name = institution_name

        if template_dir_path is not None:
            if not isinstance(template_dir_path, str):
                raise TypeError("expected template_dir_path to be a str but it is a %s" % builtins.type(template_dir_path))
        self.__template_dir_path = template_dir_path

        if theme_css_file_path is not None:
            if not isinstance(theme_css_file_path, str):
                raise TypeError("expected theme_css_file_path to be a str but it is a %s" % builtins.type(theme_css_file_path))
        self.__theme_css_file_path = theme_css_file_path

    def __eq__(self, other):
        if self.base_url != other.base_url:
            return False
        if self.copyright_holder != other.copyright_holder:
            return False
        if self.name != other.name:
            return False
        if self.output_dir_path != other.output_dir_path:
            return False
        if self.featured_searches != other.featured_searches:
            return False
        if self.institution_name != other.institution_name:
            return False
        if self.template_dir_path != other.template_dir_path:
            return False
        if self.theme_css_file_path != other.theme_css_file_path:
            return False
        return True

    def __hash__(self):
        return hash((self.base_url, self.copyright_holder, self.name, self.output_dir_path, self.featured_searches, self.institution_name, self.template_dir_path, self.theme_css_file_path,))

    def __iter__(self):
        return iter((self.base_url, self.copyright_holder, self.name, self.output_dir_path, self.featured_searches, self.institution_name, self.template_dir_path, self.theme_css_file_path,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('base_url=' + "'" + self.base_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('copyright_holder=' + "'" + self.copyright_holder.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('output_dir_path=' + "'" + self.output_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.featured_searches is not None:
            field_reprs.append('featured_searches=' + repr(self.featured_searches))
        if self.institution_name is not None:
            field_reprs.append('institution_name=' + "'" + self.institution_name.encode('ascii', 'replace').decode('ascii') + "'")
        if self.template_dir_path is not None:
            field_reprs.append('template_dir_path=' + "'" + self.template_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.theme_css_file_path is not None:
            field_reprs.append('theme_css_file_path=' + "'" + self.theme_css_file_path.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteConfiguration(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('base_url=' + "'" + self.base_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('copyright_holder=' + "'" + self.copyright_holder.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('output_dir_path=' + "'" + self.output_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.featured_searches is not None:
            field_reprs.append('featured_searches=' + repr(self.featured_searches))
        if self.institution_name is not None:
            field_reprs.append('institution_name=' + "'" + self.institution_name.encode('ascii', 'replace').decode('ascii') + "'")
        if self.template_dir_path is not None:
            field_reprs.append('template_dir_path=' + "'" + self.template_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.theme_css_file_path is not None:
            field_reprs.append('theme_css_file_path=' + "'" + self.theme_css_file_path.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteConfiguration(' + ', '.join(field_reprs) + ')'

    @property
    def base_url(self):
        '''
        :rtype: str
        '''

        return self.__base_url

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def copyright_holder(self):
        '''
        :rtype: str
        '''

        return self.__copyright_holder

    @property
    def featured_searches(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch)
        '''

        return self.__featured_searches

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        base_url = _dict.get("base_url")
        if base_url is None:
            raise KeyError("base_url")
        __builder.base_url = base_url

        copyright_holder = _dict.get("copyright_holder")
        if copyright_holder is None:
            copyright_holder = "Your Collection"
        __builder.copyright_holder = copyright_holder

        name = _dict.get("name")
        if name is None:
            name = "Your Collection"
        __builder.name = name

        output_dir_path = _dict.get("output_dir_path")
        if output_dir_path is None:
            output_dir_path = "site"
        __builder.output_dir_path = output_dir_path

        featured_searches = _dict.get("featured_searches")
        if featured_searches is not None:
            featured_searches = tuple(pastpy.gen.site.site_featured_search.SiteFeaturedSearch.from_builtins(element0) for element0 in featured_searches)
        __builder.featured_searches = featured_searches

        __builder.institution_name = _dict.get("institution_name")

        __builder.template_dir_path = _dict.get("template_dir_path")

        __builder.theme_css_file_path = _dict.get("theme_css_file_path")

        return __builder.build()

    @property
    def institution_name(self):
        '''
        :rtype: str
        '''

        return self.__institution_name

    @property
    def name(self):
        '''
        :rtype: str
        '''

        return self.__name

    @property
    def output_dir_path(self):
        '''
        :rtype: str
        '''

        return self.__output_dir_path

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'base_url':
                init_kwds['base_url'] = iprot.read_string()
            elif ifield_name == 'copyright_holder':
                init_kwds['copyright_holder'] = iprot.read_string()
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'output_dir_path':
                init_kwds['output_dir_path'] = iprot.read_string()
            elif ifield_name == 'featured_searches':
                init_kwds['featured_searches'] = tuple([pastpy.gen.site.site_featured_search.SiteFeaturedSearch.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'institution_name':
                try:
                    init_kwds['institution_name'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'template_dir_path':
                try:
                    init_kwds['template_dir_path'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'theme_css_file_path':
                try:
                    init_kwds['theme_css_file_path'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def template_dir_path(self):
        '''
        :rtype: str
        '''

        return self.__template_dir_path

    @property
    def theme_css_file_path(self):
        '''
        :rtype: str
        '''

        return self.__theme_css_file_path

    def to_builtins(self):
        dict_ = {}
        dict_["base_url"] = self.base_url
        dict_["copyright_holder"] = self.copyright_holder
        dict_["name"] = self.name
        dict_["output_dir_path"] = self.output_dir_path
        if self.featured_searches is not None:
            dict_["featured_searches"] = tuple(element0.to_builtins() for element0 in self.featured_searches)
        dict_["institution_name"] = self.institution_name
        dict_["template_dir_path"] = self.template_dir_path
        dict_["theme_css_file_path"] = self.theme_css_file_path
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        oprot.write_struct_begin('SiteConfiguration')

        oprot.write_field_begin(name='base_url', type=11, id=None)
        oprot.write_string(self.base_url)
        oprot.write_field_end()

        oprot.write_field_begin(name='copyright_holder', type=11, id=None)
        oprot.write_string(self.copyright_holder)
        oprot.write_field_end()

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='output_dir_path', type=11, id=None)
        oprot.write_string(self.output_dir_path)
        oprot.write_field_end()

        if self.featured_searches is not None:
            oprot.write_field_begin(name='featured_searches', type=15, id=None)
            oprot.write_list_begin(12, len(self.featured_searches))
            for _0 in self.featured_searches:
                _0.write(oprot)
            oprot.write_list_end()
            oprot.write_field_end()

        if self.institution_name is not None:
            oprot.write_field_begin(name='institution_name', type=11, id=None)
            oprot.write_string(self.institution_name)
            oprot.write_field_end()

        if self.template_dir_path is not None:
            oprot.write_field_begin(name='template_dir_path', type=11, id=None)
            oprot.write_string(self.template_dir_path)
            oprot.write_field_end()

        if self.theme_css_file_path is not None:
            oprot.write_field_begin(name='theme_css_file_path', type=11, id=None)
            oprot.write_string(self.theme_css_file_path)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
