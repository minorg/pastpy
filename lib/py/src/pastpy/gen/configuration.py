import builtins
import pastpy.gen.database.database_configuration
import pastpy.gen.site.site_configuration


class Configuration(object):
    class Builder(object):
        def __init__(
            self,
            database=None,
            site=None,
        ):
            '''
            :type database: pastpy.gen.database.database_configuration.DatabaseConfiguration
            :type site: pastpy.gen.site.site_configuration.SiteConfiguration or None
            '''

            self.__database = database
            self.__site = site

        def build(self):
            return Configuration(database=self.__database, site=self.__site)

        @property
        def database(self):
            '''
            :rtype: pastpy.gen.database.database_configuration.DatabaseConfiguration
            '''

            return self.__database

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.configuration.Configuration
            :rtype: pastpy.gen.configuration.Configuration
            '''

            builder = cls()
            builder.database = template.database
            builder.site = template.site
            return builder

        def set_database(self, database):
            '''
            :type database: pastpy.gen.database.database_configuration.DatabaseConfiguration
            '''

            if database is None:
                raise ValueError('database is required')
            if not isinstance(database, pastpy.gen.database.database_configuration.DatabaseConfiguration):
                raise TypeError("expected database to be a pastpy.gen.database.database_configuration.DatabaseConfiguration but it is a %s" % builtins.type(database))
            self.__database = database
            return self

        def set_site(self, site):
            '''
            :type site: pastpy.gen.site.site_configuration.SiteConfiguration or None
            '''

            if site is not None:
                if not isinstance(site, pastpy.gen.site.site_configuration.SiteConfiguration):
                    raise TypeError("expected site to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(site))
            self.__site = site
            return self

        @property
        def site(self):
            '''
            :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
            '''

            return self.__site

        def update(self, configuration):
            '''
            :type database: pastpy.gen.database.database_configuration.DatabaseConfiguration
            :type site: pastpy.gen.site.site_configuration.SiteConfiguration or None
            '''

            if isinstance(configuration, Configuration):
                self.set_database(configuration.database)
                self.set_site(configuration.site)
            elif isinstance(configuration, dict):
                for key, value in configuration.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(configuration)
            return self

        @database.setter
        def database(self, database):
            '''
            :type database: pastpy.gen.database.database_configuration.DatabaseConfiguration
            '''

            self.set_database(database)

        @site.setter
        def site(self, site):
            '''
            :type site: pastpy.gen.site.site_configuration.SiteConfiguration or None
            '''

            self.set_site(site)

    class FieldMetadata(object):
        DATABASE = None
        SITE = None

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
            return (cls.DATABASE, cls.SITE,)

    FieldMetadata.DATABASE = FieldMetadata('database', pastpy.gen.database.database_configuration.DatabaseConfiguration, None)
    FieldMetadata.SITE = FieldMetadata('site', pastpy.gen.site.site_configuration.SiteConfiguration, None)

    def __init__(
        self,
        database,
        site=None,
    ):
        '''
        :type database: pastpy.gen.database.database_configuration.DatabaseConfiguration
        :type site: pastpy.gen.site.site_configuration.SiteConfiguration or None
        '''

        if database is None:
            raise ValueError('database is required')
        if not isinstance(database, pastpy.gen.database.database_configuration.DatabaseConfiguration):
            raise TypeError("expected database to be a pastpy.gen.database.database_configuration.DatabaseConfiguration but it is a %s" % builtins.type(database))
        self.__database = database

        if site is not None:
            if not isinstance(site, pastpy.gen.site.site_configuration.SiteConfiguration):
                raise TypeError("expected site to be a pastpy.gen.site.site_configuration.SiteConfiguration but it is a %s" % builtins.type(site))
        self.__site = site

    def __eq__(self, other):
        if self.database != other.database:
            return False
        if self.site != other.site:
            return False
        return True

    def __hash__(self):
        return hash((self.database, self.site,))

    def __iter__(self):
        return iter((self.database, self.site,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('database=' + repr(self.database))
        if self.site is not None:
            field_reprs.append('site=' + repr(self.site))
        return 'Configuration(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('database=' + repr(self.database))
        if self.site is not None:
            field_reprs.append('site=' + repr(self.site))
        return 'Configuration(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def database(self):
        '''
        :rtype: pastpy.gen.database.database_configuration.DatabaseConfiguration
        '''

        return self.__database

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        database = _dict.get("database")
        if database is None:
            raise KeyError("database")
        database = pastpy.gen.database.database_configuration.DatabaseConfiguration.from_builtins(database)
        __builder.database = database

        site = _dict.get("site")
        if site is not None:
            site = pastpy.gen.site.site_configuration.SiteConfiguration.from_builtins(site)
        __builder.site = site

        return __builder.build()

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.configuration.Configuration
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'database':
                init_kwds['database'] = pastpy.gen.database.database_configuration.DatabaseConfiguration.read(iprot)
            elif ifield_name == 'site':
                init_kwds['site'] = pastpy.gen.site.site_configuration.SiteConfiguration.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    @classmethod
    def replacer(cls):
        return cls.Builder.from_template(template=self)

    @property
    def site(self):
        '''
        :rtype: pastpy.gen.site.site_configuration.SiteConfiguration
        '''

        return self.__site

    def to_builtins(self):
        dict_ = {}
        dict_["database"] = self.database.to_builtins()
        if self.site is not None:
            dict_["site"] = self.site.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.configuration.Configuration
        '''

        oprot.write_struct_begin('Configuration')

        oprot.write_field_begin(name='database', type=12, id=None)
        self.database.write(oprot)
        oprot.write_field_end()

        if self.site is not None:
            oprot.write_field_begin(name='site', type=12, id=None)
            self.site.write(oprot)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
