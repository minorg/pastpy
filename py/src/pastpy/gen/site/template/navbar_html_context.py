import builtins
import pastpy.gen.true_bool


class NavbarHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            home=None,
            objects=None,
        ):
            '''
            :type home: bool or None
            :type objects: bool or None
            '''

            self.__home = home
            self.__objects = objects

        def build(self):
            return NavbarHtmlContext(home=self.__home, objects=self.__objects)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            builder = cls()
            builder.home = template.home
            builder.objects = template.objects
            return builder

        @property
        def home(self):
            '''
            :rtype: bool
            '''

            return self.__home

        @property
        def objects(self):
            '''
            :rtype: bool
            '''

            return self.__objects

        def set_home(self, home):
            '''
            :type home: bool or None
            '''

            if home is not None:
                if not isinstance(home, bool):
                    raise TypeError("expected home to be a bool but it is a %s" % builtins.type(home))
            self.__home = home
            return self

        def set_objects(self, objects):
            '''
            :type objects: bool or None
            '''

            if objects is not None:
                if not isinstance(objects, bool):
                    raise TypeError("expected objects to be a bool but it is a %s" % builtins.type(objects))
            self.__objects = objects
            return self

        def update(self, navbar_html_context):
            '''
            :type home: bool or None
            :type objects: bool or None
            '''

            if isinstance(navbar_html_context, NavbarHtmlContext):
                self.set_home(navbar_html_context.home)
                self.set_objects(navbar_html_context.objects)
            elif isinstance(navbar_html_context, dict):
                for key, value in navbar_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(navbar_html_context)
            return self

        @home.setter
        def home(self, home):
            '''
            :type home: bool or None
            '''

            self.set_home(home)

        @objects.setter
        def objects(self, objects):
            '''
            :type objects: bool or None
            '''

            self.set_objects(objects)

    class FieldMetadata(object):
        HOME = None
        OBJECTS = None

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
            return (cls.HOME, cls.OBJECTS,)

    FieldMetadata.HOME = FieldMetadata('home', pastpy.gen.true_bool.TrueBool, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', pastpy.gen.true_bool.TrueBool, None)

    def __init__(
        self,
        home=None,
        objects=None,
    ):
        '''
        :type home: bool or None
        :type objects: bool or None
        '''

        if home is not None:
            if not isinstance(home, bool):
                raise TypeError("expected home to be a bool but it is a %s" % builtins.type(home))
        self.__home = home

        if objects is not None:
            if not isinstance(objects, bool):
                raise TypeError("expected objects to be a bool but it is a %s" % builtins.type(objects))
        self.__objects = objects

        # Union check
        __present_field_count = 0
        if self.home is not None:
            __present_field_count = __present_field_count + 1
        if self.objects is not None:
            __present_field_count = __present_field_count + 1
        if __present_field_count != 1:
            raise ValueError("navbar_html_context.NavbarHtmlContext: %d fields set in a union" % __present_field_count)

    def __eq__(self, other):
        if self.home != other.home:
            return False
        if self.objects != other.objects:
            return False
        return True

    def __hash__(self):
        return hash((self.home, self.objects,))

    def __iter__(self):
        return iter((self.home, self.objects,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        if self.home is not None:
            field_reprs.append('home=' + repr(self.home))
        if self.objects is not None:
            field_reprs.append('objects=' + repr(self.objects))
        return 'NavbarHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.home is not None:
            field_reprs.append('home=' + repr(self.home))
        if self.objects is not None:
            field_reprs.append('objects=' + repr(self.objects))
        return 'NavbarHtmlContext(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        __builder.home = _dict.get("home")

        __builder.objects = _dict.get("objects")

        return __builder.build()

    @property
    def home(self):
        '''
        :rtype: bool
        '''

        return self.__home

    @property
    def objects(self):
        '''
        :rtype: bool
        '''

        return self.__objects

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'home':
                try:
                    init_kwds['home'] = iprot.read_bool()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objects':
                try:
                    init_kwds['objects'] = iprot.read_bool()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["home"] = self.home
        dict_["objects"] = self.objects
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        '''

        oprot.write_struct_begin('NavbarHtmlContext')

        if self.home is not None:
            oprot.write_field_begin(name='home', type=2, id=None)
            oprot.write_bool(self.home)
            oprot.write_field_end()

        if self.objects is not None:
            oprot.write_field_begin(name='objects', type=2, id=None)
            oprot.write_bool(self.objects)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
