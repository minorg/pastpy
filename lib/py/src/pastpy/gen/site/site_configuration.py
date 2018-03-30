import builtins
import pastpy.gen.non_blank_string


class SiteConfiguration(object):
    class Builder(object):
        def __init__(
            self,
            copyright_holder="Your Collection",
            google_custom_search_engine_id=None,
            name="Your Collection",
            output_dir_path="site",
            institution_name=None,
            template_dir_path=None,
        ):
            '''
            :type copyright_holder: str
            :type google_custom_search_engine_id: str
            :type name: str
            :type output_dir_path: str
            :type institution_name: str or None
            :type template_dir_path: str or None
            '''

            self.__copyright_holder = copyright_holder
            self.__google_custom_search_engine_id = google_custom_search_engine_id
            self.__name = name
            self.__output_dir_path = output_dir_path
            self.__institution_name = institution_name
            self.__template_dir_path = template_dir_path

        def build(self):
            return SiteConfiguration(copyright_holder=self.__copyright_holder, google_custom_search_engine_id=self.__google_custom_search_engine_id, name=self.__name, output_dir_path=self.__output_dir_path, institution_name=self.__institution_name, template_dir_path=self.__template_dir_path)

        @property
        def copyright_holder(self):
            '''
            :rtype: str
            '''

            return self.__copyright_holder

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_configuration.SiteConfiguration
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            builder = cls()
            builder.copyright_holder = template.copyright_holder
            builder.google_custom_search_engine_id = template.google_custom_search_engine_id
            builder.name = template.name
            builder.output_dir_path = template.output_dir_path
            builder.institution_name = template.institution_name
            builder.template_dir_path = template.template_dir_path
            return builder

        @property
        def google_custom_search_engine_id(self):
            '''
            :rtype: str
            '''

            return self.__google_custom_search_engine_id

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

        def set_google_custom_search_engine_id(self, google_custom_search_engine_id):
            '''
            :type google_custom_search_engine_id: str
            '''

            if google_custom_search_engine_id is None:
                raise ValueError('google_custom_search_engine_id is required')
            if not isinstance(google_custom_search_engine_id, str):
                raise TypeError("expected google_custom_search_engine_id to be a str but it is a %s" % builtins.type(google_custom_search_engine_id))
            self.__google_custom_search_engine_id = google_custom_search_engine_id
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

        @property
        def template_dir_path(self):
            '''
            :rtype: str
            '''

            return self.__template_dir_path

        def update(self, site_configuration):
            '''
            :type copyright_holder: str
            :type google_custom_search_engine_id: str
            :type name: str
            :type output_dir_path: str
            :type institution_name: str or None
            :type template_dir_path: str or None
            '''

            if isinstance(site_configuration, SiteConfiguration):
                self.set_copyright_holder(site_configuration.copyright_holder)
                self.set_google_custom_search_engine_id(site_configuration.google_custom_search_engine_id)
                self.set_name(site_configuration.name)
                self.set_output_dir_path(site_configuration.output_dir_path)
                self.set_institution_name(site_configuration.institution_name)
                self.set_template_dir_path(site_configuration.template_dir_path)
            elif isinstance(site_configuration, dict):
                for key, value in site_configuration.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_configuration)
            return self

        @copyright_holder.setter
        def copyright_holder(self, copyright_holder):
            '''
            :type copyright_holder: str
            '''

            self.set_copyright_holder(copyright_holder)

        @google_custom_search_engine_id.setter
        def google_custom_search_engine_id(self, google_custom_search_engine_id):
            '''
            :type google_custom_search_engine_id: str
            '''

            self.set_google_custom_search_engine_id(google_custom_search_engine_id)

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

    class FieldMetadata(object):
        COPYRIGHT_HOLDER = None
        GOOGLE_CUSTOM_SEARCH_ENGINE_ID = None
        NAME = None
        OUTPUT_DIR_PATH = None
        INSTITUTION_NAME = None
        TEMPLATE_DIR_PATH = None

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
            return (cls.COPYRIGHT_HOLDER, cls.GOOGLE_CUSTOM_SEARCH_ENGINE_ID, cls.NAME, cls.OUTPUT_DIR_PATH, cls.INSTITUTION_NAME, cls.TEMPLATE_DIR_PATH,)

    FieldMetadata.COPYRIGHT_HOLDER = FieldMetadata('copyright_holder', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.GOOGLE_CUSTOM_SEARCH_ENGINE_ID = FieldMetadata('google_custom_search_engine_id', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.NAME = FieldMetadata('name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.OUTPUT_DIR_PATH = FieldMetadata('output_dir_path', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.INSTITUTION_NAME = FieldMetadata('institution_name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.TEMPLATE_DIR_PATH = FieldMetadata('template_dir_path', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        google_custom_search_engine_id,
        copyright_holder="Your Collection",
        name="Your Collection",
        output_dir_path="site",
        institution_name=None,
        template_dir_path=None,
    ):
        '''
        :type copyright_holder: str
        :type google_custom_search_engine_id: str
        :type name: str
        :type output_dir_path: str
        :type institution_name: str or None
        :type template_dir_path: str or None
        '''

        if copyright_holder is None:
            raise ValueError('copyright_holder is required')
        if not isinstance(copyright_holder, str):
            raise TypeError("expected copyright_holder to be a str but it is a %s" % builtins.type(copyright_holder))
        self.__copyright_holder = copyright_holder

        if google_custom_search_engine_id is None:
            raise ValueError('google_custom_search_engine_id is required')
        if not isinstance(google_custom_search_engine_id, str):
            raise TypeError("expected google_custom_search_engine_id to be a str but it is a %s" % builtins.type(google_custom_search_engine_id))
        self.__google_custom_search_engine_id = google_custom_search_engine_id

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

        if institution_name is not None:
            if not isinstance(institution_name, str):
                raise TypeError("expected institution_name to be a str but it is a %s" % builtins.type(institution_name))
        self.__institution_name = institution_name

        if template_dir_path is not None:
            if not isinstance(template_dir_path, str):
                raise TypeError("expected template_dir_path to be a str but it is a %s" % builtins.type(template_dir_path))
        self.__template_dir_path = template_dir_path

    def __eq__(self, other):
        if self.copyright_holder != other.copyright_holder:
            return False
        if self.google_custom_search_engine_id != other.google_custom_search_engine_id:
            return False
        if self.name != other.name:
            return False
        if self.output_dir_path != other.output_dir_path:
            return False
        if self.institution_name != other.institution_name:
            return False
        if self.template_dir_path != other.template_dir_path:
            return False
        return True

    def __hash__(self):
        return hash((self.copyright_holder, self.google_custom_search_engine_id, self.name, self.output_dir_path, self.institution_name, self.template_dir_path,))

    def __iter__(self):
        return iter((self.copyright_holder, self.google_custom_search_engine_id, self.name, self.output_dir_path, self.institution_name, self.template_dir_path,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('copyright_holder=' + "'" + self.copyright_holder.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('google_custom_search_engine_id=' + "'" + self.google_custom_search_engine_id.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('output_dir_path=' + "'" + self.output_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.institution_name is not None:
            field_reprs.append('institution_name=' + "'" + self.institution_name.encode('ascii', 'replace').decode('ascii') + "'")
        if self.template_dir_path is not None:
            field_reprs.append('template_dir_path=' + "'" + self.template_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteConfiguration(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('copyright_holder=' + "'" + self.copyright_holder.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('google_custom_search_engine_id=' + "'" + self.google_custom_search_engine_id.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('output_dir_path=' + "'" + self.output_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        if self.institution_name is not None:
            field_reprs.append('institution_name=' + "'" + self.institution_name.encode('ascii', 'replace').decode('ascii') + "'")
        if self.template_dir_path is not None:
            field_reprs.append('template_dir_path=' + "'" + self.template_dir_path.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteConfiguration(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def copyright_holder(self):
        '''
        :rtype: str
        '''

        return self.__copyright_holder

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        copyright_holder = _dict.get("copyright_holder")
        if copyright_holder is None:
            copyright_holder = "Your Collection"
        __builder.copyright_holder = copyright_holder

        google_custom_search_engine_id = _dict.get("google_custom_search_engine_id")
        if google_custom_search_engine_id is None:
            raise KeyError("google_custom_search_engine_id")
        __builder.google_custom_search_engine_id = google_custom_search_engine_id

        name = _dict.get("name")
        if name is None:
            name = "Your Collection"
        __builder.name = name

        output_dir_path = _dict.get("output_dir_path")
        if output_dir_path is None:
            output_dir_path = "site"
        __builder.output_dir_path = output_dir_path

        __builder.institution_name = _dict.get("institution_name")

        __builder.template_dir_path = _dict.get("template_dir_path")

        return __builder.build()

    @property
    def google_custom_search_engine_id(self):
        '''
        :rtype: str
        '''

        return self.__google_custom_search_engine_id

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
            elif ifield_name == 'copyright_holder':
                init_kwds['copyright_holder'] = iprot.read_string()
            elif ifield_name == 'google_custom_search_engine_id':
                init_kwds['google_custom_search_engine_id'] = iprot.read_string()
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'output_dir_path':
                init_kwds['output_dir_path'] = iprot.read_string()
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

    def to_builtins(self):
        dict_ = {}
        dict_["copyright_holder"] = self.copyright_holder
        dict_["google_custom_search_engine_id"] = self.google_custom_search_engine_id
        dict_["name"] = self.name
        dict_["output_dir_path"] = self.output_dir_path
        dict_["institution_name"] = self.institution_name
        dict_["template_dir_path"] = self.template_dir_path
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        oprot.write_struct_begin('SiteConfiguration')

        oprot.write_field_begin(name='copyright_holder', type=11, id=None)
        oprot.write_string(self.copyright_holder)
        oprot.write_field_end()

        oprot.write_field_begin(name='google_custom_search_engine_id', type=11, id=None)
        oprot.write_string(self.google_custom_search_engine_id)
        oprot.write_field_end()

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='output_dir_path', type=11, id=None)
        oprot.write_string(self.output_dir_path)
        oprot.write_field_end()

        if self.institution_name is not None:
            oprot.write_field_begin(name='institution_name', type=11, id=None)
            oprot.write_string(self.institution_name)
            oprot.write_field_end()

        if self.template_dir_path is not None:
            oprot.write_field_begin(name='template_dir_path', type=11, id=None)
            oprot.write_string(self.template_dir_path)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
