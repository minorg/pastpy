import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_object
import pastpy.gen.site.template.footer_html_context
import pastpy.gen.site.template.navbar_html_context


class ObjectDetailHtmlContext(object):
    class Builder(object):
        def __init__(
            self,
            footer=None,
            navbar=None,
            object=None,  # @ReservedAssignment
            root_relative_href=None,
        ):
            '''
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type object: pastpy.gen.site.site_object.SiteObject
            :type root_relative_href: str
            '''

            self.__footer = footer
            self.__navbar = navbar
            self.__object = object
            self.__root_relative_href = root_relative_href

        def build(self):
            return ObjectDetailHtmlContext(footer=self.__footer, navbar=self.__navbar, object=self.__object, root_relative_href=self.__root_relative_href)

        @property
        def footer(self):
            '''
            :rtype: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            '''

            return self.__footer

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
            :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
            '''

            builder = cls()
            builder.footer = template.footer
            builder.navbar = template.navbar
            builder.object = template.object
            builder.root_relative_href = template.root_relative_href
            return builder

        @property
        def navbar(self):
            '''
            :rtype: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            '''

            return self.__navbar

        @property
        def object(self):  # @ReservedAssignment
            '''
            :rtype: pastpy.gen.site.site_object.SiteObject
            '''

            return self.__object

        @property
        def root_relative_href(self):
            '''
            :rtype: str
            '''

            return self.__root_relative_href

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

        def set_object(self, object):  # @ReservedAssignment
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            if object is None:
                raise ValueError('object is required')
            if not isinstance(object, pastpy.gen.site.site_object.SiteObject):
                raise TypeError("expected object to be a pastpy.gen.site.site_object.SiteObject but it is a %s" % builtins.type(object))
            self.__object = object
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

        def update(self, object_detail_html_context):
            '''
            :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
            :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
            :type object: pastpy.gen.site.site_object.SiteObject
            :type root_relative_href: str
            '''

            if isinstance(object_detail_html_context, ObjectDetailHtmlContext):
                self.set_footer(object_detail_html_context.footer)
                self.set_navbar(object_detail_html_context.navbar)
                self.set_object(object_detail_html_context.object)
                self.set_root_relative_href(object_detail_html_context.root_relative_href)
            elif isinstance(object_detail_html_context, dict):
                for key, value in object_detail_html_context.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(object_detail_html_context)
            return self

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

        @object.setter
        def object(self, object):  # @ReservedAssignment
            '''
            :type object: pastpy.gen.site.site_object.SiteObject
            '''

            self.set_object(object)

        @root_relative_href.setter
        def root_relative_href(self, root_relative_href):
            '''
            :type root_relative_href: str
            '''

            self.set_root_relative_href(root_relative_href)

    class FieldMetadata(object):
        FOOTER = None
        NAVBAR = None
        OBJECT = None
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
            return (cls.FOOTER, cls.NAVBAR, cls.OBJECT, cls.ROOT_RELATIVE_HREF,)

    FieldMetadata.FOOTER = FieldMetadata('footer', pastpy.gen.site.template.footer_html_context.FooterHtmlContext, None)
    FieldMetadata.NAVBAR = FieldMetadata('navbar', pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext, None)
    FieldMetadata.OBJECT = FieldMetadata('object', pastpy.gen.site.site_object.SiteObject, None)
    FieldMetadata.ROOT_RELATIVE_HREF = FieldMetadata('root_relative_href', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        footer,
        navbar,
        object,  # @ReservedAssignment
        root_relative_href,
    ):
        '''
        :type footer: pastpy.gen.site.template.footer_html_context.FooterHtmlContext
        :type navbar: pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext
        :type object: pastpy.gen.site.site_object.SiteObject
        :type root_relative_href: str
        '''

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

        if object is None:
            raise ValueError('object is required')
        if not isinstance(object, pastpy.gen.site.site_object.SiteObject):
            raise TypeError("expected object to be a pastpy.gen.site.site_object.SiteObject but it is a %s" % builtins.type(object))
        self.__object = object

        if root_relative_href is None:
            raise ValueError('root_relative_href is required')
        if not isinstance(root_relative_href, str):
            raise TypeError("expected root_relative_href to be a str but it is a %s" % builtins.type(root_relative_href))
        self.__root_relative_href = root_relative_href

    def __eq__(self, other):
        if self.footer != other.footer:
            return False
        if self.navbar != other.navbar:
            return False
        if self.object != other.object:
            return False
        if self.root_relative_href != other.root_relative_href:
            return False
        return True

    def __hash__(self):
        return hash((self.footer, self.navbar, self.object, self.root_relative_href,))

    def __iter__(self):
        return iter((self.footer, self.navbar, self.object, self.root_relative_href,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('object=' + repr(self.object))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectDetailHtmlContext(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('footer=' + repr(self.footer))
        field_reprs.append('navbar=' + repr(self.navbar))
        field_reprs.append('object=' + repr(self.object))
        field_reprs.append('root_relative_href=' + "'" + self.root_relative_href.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectDetailHtmlContext(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

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

        object = _dict.get("object")
        if object is None:
            raise KeyError("object")
        object = pastpy.gen.site.site_object.SiteObject.from_builtins(object)
        __builder.object = object

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
    def object(self):  # @ReservedAssignment
        '''
        :rtype: pastpy.gen.site.site_object.SiteObject
        '''

        return self.__object

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'footer':
                init_kwds['footer'] = pastpy.gen.site.template.footer_html_context.FooterHtmlContext.read(iprot)
            elif ifield_name == 'navbar':
                init_kwds['navbar'] = pastpy.gen.site.template.navbar_html_context.NavbarHtmlContext.read(iprot)
            elif ifield_name == 'object':
                init_kwds['object'] = pastpy.gen.site.site_object.SiteObject.read(iprot)
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
        dict_["footer"] = self.footer.to_builtins()
        dict_["navbar"] = self.navbar.to_builtins()
        dict_["object"] = self.object.to_builtins()
        dict_["root_relative_href"] = self.root_relative_href
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.template.objects.detail.object_detail_html_context.ObjectDetailHtmlContext
        '''

        oprot.write_struct_begin('ObjectDetailHtmlContext')

        oprot.write_field_begin(name='footer', type=12, id=None)
        self.footer.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='navbar', type=12, id=None)
        self.navbar.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='object', type=12, id=None)
        self.object.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='root_relative_href', type=11, id=None)
        oprot.write_string(self.root_relative_href)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
