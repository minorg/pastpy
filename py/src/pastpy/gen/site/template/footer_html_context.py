import builtins


class FooterHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            current_year=None,
        ):
            '''
            :type current_year: int
            '''

            self.__current_year = current_year

        def build(self):
            return FooterHtmlContext(current_year=self.__current_year)

        @property
        def current_year(self):
            '''
            :rtype: int
            '''

            return self.__current_year

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            '''

            builder = cls()
            builder.current_year = template.current_year
            return builder

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

        def update(self, footer_html_context):
            '''
            :type current_year: int
            '''

            if isinstance(footer_html_context, FooterHtmlContext):
                self.set_current_year(footer_html_context.current_year)
            elif isinstance(footer_html_context, dict):
                for key, value in footer_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(footer_html_context)
            return self

        @current_year.setter
        def current_year(self, current_year):
            '''
            :type current_year: int
            '''

            self.set_current_year(current_year)

    class FieldMetadata(object):
        CURRENT_YEAR = None

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
            return (cls.CURRENT_YEAR,)

    FieldMetadata.CURRENT_YEAR = FieldMetadata('current_year', int, None)

    def __init__(
        self,
        current_year,
    ):
        '''
        :type current_year: int
        '''

        if current_year is None:
            raise ValueError('current_year is required')
        if not isinstance(current_year, int):
            raise TypeError("expected current_year to be a int but it is a %s" % builtins.type(current_year))
        self.__current_year = current_year

    def __eq__(self, other):
        if self.current_year != other.current_year:
            return False
        return True

    def __hash__(self):
        return hash(self.current_year)

    def __iter__(self):
        return iter((self.current_year,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('current_year=' + repr(self.current_year))
        return 'FooterHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('current_year=' + repr(self.current_year))
        return 'FooterHtmlContext(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

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

        current_year = _dict.get("current_year")
        if current_year is None:
            raise KeyError("current_year")
        __builder.current_year = current_year

        return __builder.build()

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'current_year':
                init_kwds['current_year'] = iprot.read_i32()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["current_year"] = self.current_year
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        '''

        oprot.write_struct_begin('FooterHtmlContext')

        oprot.write_field_begin(name='current_year', type=8, id=None)
        oprot.write_i32(self.current_year)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
