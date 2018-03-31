import builtins


class SiteObjectsListPageNumber(object):
    class Builder(object):
        def __init__(
            self,
            active=None,
            enabled=None,
            number=None,
        ):
            '''
            :type active: bool
            :type enabled: bool
            :type number: int
            '''

            self.__active = active
            self.__enabled = enabled
            self.__number = number

        def build(self):
            return SiteObjectsListPageNumber(active=self.__active, enabled=self.__enabled, number=self.__number)

        @property
        def active(self):
            '''
            :rtype: bool
            '''

            return self.__active

        @property
        def enabled(self):
            '''
            :rtype: bool
            '''

            return self.__enabled

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            builder = cls()
            builder.active = template.active
            builder.enabled = template.enabled
            builder.number = template.number
            return builder

        @property
        def number(self):
            '''
            :rtype: int
            '''

            return self.__number

        def set_active(self, active):
            '''
            :type active: bool
            '''

            if active is None:
                raise ValueError('active is required')
            if not isinstance(active, bool):
                raise TypeError("expected active to be a bool but it is a %s" % builtins.type(active))
            self.__active = active
            return self

        def set_enabled(self, enabled):
            '''
            :type enabled: bool
            '''

            if enabled is None:
                raise ValueError('enabled is required')
            if not isinstance(enabled, bool):
                raise TypeError("expected enabled to be a bool but it is a %s" % builtins.type(enabled))
            self.__enabled = enabled
            return self

        def set_number(self, number):
            '''
            :type number: int
            '''

            if number is None:
                raise ValueError('number is required')
            if not isinstance(number, int):
                raise TypeError("expected number to be a int but it is a %s" % builtins.type(number))
            if number < 1:
                raise ValueError("expected number to be >= 1, was %s" % number)
            self.__number = number
            return self

        def update(self, site_objects_list_page_number):
            '''
            :type active: bool
            :type enabled: bool
            :type number: int
            '''

            if isinstance(site_objects_list_page_number, SiteObjectsListPageNumber):
                self.set_active(site_objects_list_page_number.active)
                self.set_enabled(site_objects_list_page_number.enabled)
                self.set_number(site_objects_list_page_number.number)
            elif isinstance(site_objects_list_page_number, dict):
                for key, value in site_objects_list_page_number.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_objects_list_page_number)
            return self

        @active.setter
        def active(self, active):
            '''
            :type active: bool
            '''

            self.set_active(active)

        @enabled.setter
        def enabled(self, enabled):
            '''
            :type enabled: bool
            '''

            self.set_enabled(enabled)

        @number.setter
        def number(self, number):
            '''
            :type number: int
            '''

            self.set_number(number)

    class FieldMetadata(object):
        ACTIVE = None
        ENABLED = None
        NUMBER = None

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
            return (cls.ACTIVE, cls.ENABLED, cls.NUMBER,)

    FieldMetadata.ACTIVE = FieldMetadata('active', bool, None)
    FieldMetadata.ENABLED = FieldMetadata('enabled', bool, None)
    FieldMetadata.NUMBER = FieldMetadata('number', int, OrderedDict([('min', 1)]))

    def __init__(
        self,
        active,
        enabled,
        number,
    ):
        '''
        :type active: bool
        :type enabled: bool
        :type number: int
        '''

        if active is None:
            raise ValueError('active is required')
        if not isinstance(active, bool):
            raise TypeError("expected active to be a bool but it is a %s" % builtins.type(active))
        self.__active = active

        if enabled is None:
            raise ValueError('enabled is required')
        if not isinstance(enabled, bool):
            raise TypeError("expected enabled to be a bool but it is a %s" % builtins.type(enabled))
        self.__enabled = enabled

        if number is None:
            raise ValueError('number is required')
        if not isinstance(number, int):
            raise TypeError("expected number to be a int but it is a %s" % builtins.type(number))
        if number < 1:
            raise ValueError("expected number to be >= 1, was %s" % number)
        self.__number = number

    def __eq__(self, other):
        if self.active != other.active:
            return False
        if self.enabled != other.enabled:
            return False
        if self.number != other.number:
            return False
        return True

    def __hash__(self):
        return hash((self.active, self.enabled, self.number,))

    def __iter__(self):
        return iter((self.active, self.enabled, self.number,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('active=' + repr(self.active))
        field_reprs.append('enabled=' + repr(self.enabled))
        field_reprs.append('number=' + repr(self.number))
        return 'SiteObjectsListPageNumber(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('active=' + repr(self.active))
        field_reprs.append('enabled=' + repr(self.enabled))
        field_reprs.append('number=' + repr(self.number))
        return 'SiteObjectsListPageNumber(' + ', '.join(field_reprs) + ')'

    @property
    def active(self):
        '''
        :rtype: bool
        '''

        return self.__active

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def enabled(self):
        '''
        :rtype: bool
        '''

        return self.__enabled

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        active = _dict.get("active")
        if active is None:
            raise KeyError("active")
        __builder.active = active

        enabled = _dict.get("enabled")
        if enabled is None:
            raise KeyError("enabled")
        __builder.enabled = enabled

        number = _dict.get("number")
        if number is None:
            raise KeyError("number")
        __builder.number = number

        return __builder.build()

    @property
    def number(self):
        '''
        :rtype: int
        '''

        return self.__number

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'active':
                init_kwds['active'] = iprot.read_bool()
            elif ifield_name == 'enabled':
                init_kwds['enabled'] = iprot.read_bool()
            elif ifield_name == 'number':
                init_kwds['number'] = iprot.read_i32()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["active"] = self.active
        dict_["enabled"] = self.enabled
        dict_["number"] = self.number
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        '''

        oprot.write_struct_begin('SiteObjectsListPageNumber')

        oprot.write_field_begin(name='active', type=2, id=None)
        oprot.write_bool(self.active)
        oprot.write_field_end()

        oprot.write_field_begin(name='enabled', type=2, id=None)
        oprot.write_bool(self.enabled)
        oprot.write_field_end()

        oprot.write_field_begin(name='number', type=8, id=None)
        oprot.write_i32(self.number)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
