from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_nav_items
import pastpy.gen.site.site_object
import pastpy.gen.site.site_objects_list_page_number


class SiteObjectsListPage(object):
    class Builder(object):
        def __init__(
            self,
            absolute_href=None,
            nav_items=None,
            next_page_number=None,
            objects=None,
            page_numbers=None,
            previous_page_number=None,
        ):
            '''
            :type absolute_href: str
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            self.__absolute_href = absolute_href
            self.__nav_items = nav_items
            self.__next_page_number = next_page_number
            self.__objects = objects
            self.__page_numbers = page_numbers
            self.__previous_page_number = previous_page_number

        def build(self):
            return SiteObjectsListPage(absolute_href=self.__absolute_href, nav_items=self.__nav_items, next_page_number=self.__next_page_number, objects=self.__objects, page_numbers=self.__page_numbers, previous_page_number=self.__previous_page_number)

        @property
        def absolute_href(self):
            '''
            :rtype: str
            '''

            return self.__absolute_href

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_objects_list_page.SiteObjectsListPage
            :rtype: pastpy.gen.site.site_objects_list_page.SiteObjectsListPage
            '''

            builder = cls()
            builder.absolute_href = template.absolute_href
            builder.nav_items = template.nav_items
            builder.next_page_number = template.next_page_number
            builder.objects = template.objects
            builder.page_numbers = template.page_numbers
            builder.previous_page_number = template.previous_page_number
            return builder

        @property
        def nav_items(self):
            '''
            :rtype: pastpy.gen.site.site_nav_items.SiteNavItems
            '''

            return self.__nav_items

        @property
        def next_page_number(self):
            '''
            :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            return self.__next_page_number

        @property
        def objects(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            return self.__objects

        @property
        def page_numbers(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            return self.__page_numbers

        @property
        def previous_page_number(self):
            '''
            :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            return self.__previous_page_number

        def set_absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            if absolute_href is None:
                raise ValueError('absolute_href is required')
            if not isinstance(absolute_href, str):
                raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
            self.__absolute_href = absolute_href
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

        def set_next_page_number(self, next_page_number):
            '''
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            if next_page_number is None:
                raise ValueError('next_page_number is required')
            if not isinstance(next_page_number, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber):
                raise TypeError("expected next_page_number to be a pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber but it is a %s" % builtins.type(next_page_number))
            self.__next_page_number = next_page_number
            return self

        def set_objects(self, objects):
            '''
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            if objects is None:
                raise ValueError('objects is required')
            if not (isinstance(objects, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_object.SiteObject), objects))) == 0):
                raise TypeError("expected objects to be a tuple(pastpy.gen.site.site_object.SiteObject) but it is a %s" % builtins.type(objects))
            self.__objects = objects
            return self

        def set_page_numbers(self, page_numbers):
            '''
            :type page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            if page_numbers is None:
                raise ValueError('page_numbers is required')
            if not (isinstance(page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber), page_numbers))) == 0):
                raise TypeError("expected page_numbers to be a tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber) but it is a %s" % builtins.type(page_numbers))
            self.__page_numbers = page_numbers
            return self

        def set_previous_page_number(self, previous_page_number):
            '''
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            if previous_page_number is None:
                raise ValueError('previous_page_number is required')
            if not isinstance(previous_page_number, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber):
                raise TypeError("expected previous_page_number to be a pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber but it is a %s" % builtins.type(previous_page_number))
            self.__previous_page_number = previous_page_number
            return self

        def update(self, site_objects_list_page):
            '''
            :type absolute_href: str
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            if isinstance(site_objects_list_page, SiteObjectsListPage):
                self.set_absolute_href(site_objects_list_page.absolute_href)
                self.set_nav_items(site_objects_list_page.nav_items)
                self.set_next_page_number(site_objects_list_page.next_page_number)
                self.set_objects(site_objects_list_page.objects)
                self.set_page_numbers(site_objects_list_page.page_numbers)
                self.set_previous_page_number(site_objects_list_page.previous_page_number)
            elif isinstance(site_objects_list_page, dict):
                for key, value in site_objects_list_page.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_objects_list_page)
            return self

        @absolute_href.setter
        def absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            self.set_absolute_href(absolute_href)

        @nav_items.setter
        def nav_items(self, nav_items):
            '''
            :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
            '''

            self.set_nav_items(nav_items)

        @next_page_number.setter
        def next_page_number(self, next_page_number):
            '''
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            self.set_next_page_number(next_page_number)

        @objects.setter
        def objects(self, objects):
            '''
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            '''

            self.set_objects(objects)

        @page_numbers.setter
        def page_numbers(self, page_numbers):
            '''
            :type page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            self.set_page_numbers(page_numbers)

        @previous_page_number.setter
        def previous_page_number(self, previous_page_number):
            '''
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            self.set_previous_page_number(previous_page_number)

    class FieldMetadata(object):
        ABSOLUTE_HREF = None
        NAV_ITEMS = None
        NEXT_PAGE_NUMBER = None
        OBJECTS = None
        PAGE_NUMBERS = None
        PREVIOUS_PAGE_NUMBER = None

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
            return (cls.ABSOLUTE_HREF, cls.NAV_ITEMS, cls.NEXT_PAGE_NUMBER, cls.OBJECTS, cls.PAGE_NUMBERS, cls.PREVIOUS_PAGE_NUMBER,)

    FieldMetadata.ABSOLUTE_HREF = FieldMetadata('absolute_href', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.NAV_ITEMS = FieldMetadata('nav_items', pastpy.gen.site.site_nav_items.SiteNavItems, None)
    FieldMetadata.NEXT_PAGE_NUMBER = FieldMetadata('next_page_number', pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.PAGE_NUMBERS = FieldMetadata('page_numbers', tuple, None)
    FieldMetadata.PREVIOUS_PAGE_NUMBER = FieldMetadata('previous_page_number', pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber, None)

    def __init__(
        self,
        absolute_href,
        nav_items,
        next_page_number,
        objects,
        page_numbers,
        previous_page_number,
    ):
        '''
        :type absolute_href: str
        :type nav_items: pastpy.gen.site.site_nav_items.SiteNavItems
        :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
        :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        '''

        if absolute_href is None:
            raise ValueError('absolute_href is required')
        if not isinstance(absolute_href, str):
            raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
        self.__absolute_href = absolute_href

        if nav_items is None:
            raise ValueError('nav_items is required')
        if not isinstance(nav_items, pastpy.gen.site.site_nav_items.SiteNavItems):
            raise TypeError("expected nav_items to be a pastpy.gen.site.site_nav_items.SiteNavItems but it is a %s" % builtins.type(nav_items))
        self.__nav_items = nav_items

        if next_page_number is None:
            raise ValueError('next_page_number is required')
        if not isinstance(next_page_number, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber):
            raise TypeError("expected next_page_number to be a pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber but it is a %s" % builtins.type(next_page_number))
        self.__next_page_number = next_page_number

        if objects is None:
            raise ValueError('objects is required')
        if not (isinstance(objects, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_object.SiteObject), objects))) == 0):
            raise TypeError("expected objects to be a tuple(pastpy.gen.site.site_object.SiteObject) but it is a %s" % builtins.type(objects))
        self.__objects = objects

        if page_numbers is None:
            raise ValueError('page_numbers is required')
        if not (isinstance(page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber), page_numbers))) == 0):
            raise TypeError("expected page_numbers to be a tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber) but it is a %s" % builtins.type(page_numbers))
        self.__page_numbers = page_numbers

        if previous_page_number is None:
            raise ValueError('previous_page_number is required')
        if not isinstance(previous_page_number, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber):
            raise TypeError("expected previous_page_number to be a pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber but it is a %s" % builtins.type(previous_page_number))
        self.__previous_page_number = previous_page_number

    def __eq__(self, other):
        if self.absolute_href != other.absolute_href:
            return False
        if self.nav_items != other.nav_items:
            return False
        if self.next_page_number != other.next_page_number:
            return False
        if self.objects != other.objects:
            return False
        if self.page_numbers != other.page_numbers:
            return False
        if self.previous_page_number != other.previous_page_number:
            return False
        return True

    def __hash__(self):
        return hash((self.absolute_href, self.nav_items, self.next_page_number, self.objects, self.page_numbers, self.previous_page_number,))

    def __iter__(self):
        return iter((self.absolute_href, self.nav_items, self.next_page_number, self.objects, self.page_numbers, self.previous_page_number,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('nav_items=' + repr(self.nav_items))
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('page_numbers=' + repr(self.page_numbers))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        return 'SiteObjectsListPage(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('nav_items=' + repr(self.nav_items))
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('page_numbers=' + repr(self.page_numbers))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        return 'SiteObjectsListPage(' + ', '.join(field_reprs) + ')'

    @property
    def absolute_href(self):
        '''
        :rtype: str
        '''

        return self.__absolute_href

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        absolute_href = _dict.get("absolute_href")
        if absolute_href is None:
            raise KeyError("absolute_href")
        __builder.absolute_href = absolute_href

        nav_items = _dict.get("nav_items")
        if nav_items is None:
            raise KeyError("nav_items")
        nav_items = pastpy.gen.site.site_nav_items.SiteNavItems.from_builtins(nav_items)
        __builder.nav_items = nav_items

        next_page_number = _dict.get("next_page_number")
        if next_page_number is None:
            raise KeyError("next_page_number")
        next_page_number = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.from_builtins(next_page_number)
        __builder.next_page_number = next_page_number

        objects = _dict.get("objects")
        if objects is None:
            raise KeyError("objects")
        objects = tuple(pastpy.gen.site.site_object.SiteObject.from_builtins(element0) for element0 in objects)
        __builder.objects = objects

        page_numbers = _dict.get("page_numbers")
        if page_numbers is None:
            raise KeyError("page_numbers")
        page_numbers = tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.from_builtins(element0) for element0 in page_numbers)
        __builder.page_numbers = page_numbers

        previous_page_number = _dict.get("previous_page_number")
        if previous_page_number is None:
            raise KeyError("previous_page_number")
        previous_page_number = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.from_builtins(previous_page_number)
        __builder.previous_page_number = previous_page_number

        return __builder.build()

    @property
    def nav_items(self):
        '''
        :rtype: pastpy.gen.site.site_nav_items.SiteNavItems
        '''

        return self.__nav_items

    @property
    def next_page_number(self):
        '''
        :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        '''

        return self.__next_page_number

    @property
    def objects(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_object.SiteObject)
        '''

        return self.__objects

    @property
    def page_numbers(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
        '''

        return self.__page_numbers

    @property
    def previous_page_number(self):
        '''
        :rtype: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        '''

        return self.__previous_page_number

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_objects_list_page.SiteObjectsListPage
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'absolute_href':
                init_kwds['absolute_href'] = iprot.read_string()
            elif ifield_name == 'nav_items':
                init_kwds['nav_items'] = pastpy.gen.site.site_nav_items.SiteNavItems.read(iprot)
            elif ifield_name == 'next_page_number':
                init_kwds['next_page_number'] = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot)
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'page_numbers':
                init_kwds['page_numbers'] = tuple([pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'previous_page_number':
                init_kwds['previous_page_number'] = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["absolute_href"] = self.absolute_href
        dict_["nav_items"] = self.nav_items.to_builtins()
        dict_["next_page_number"] = self.next_page_number.to_builtins()
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["page_numbers"] = tuple(element0.to_builtins() for element0 in self.page_numbers)
        dict_["previous_page_number"] = self.previous_page_number.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_objects_list_page.SiteObjectsListPage
        '''

        oprot.write_struct_begin('SiteObjectsListPage')

        oprot.write_field_begin(name='absolute_href', type=11, id=None)
        oprot.write_string(self.absolute_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='nav_items', type=12, id=None)
        self.nav_items.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='next_page_number', type=12, id=None)
        self.next_page_number.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='objects', type=15, id=None)
        oprot.write_list_begin(12, len(self.objects))
        for _0 in self.objects:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='page_numbers', type=15, id=None)
        oprot.write_list_begin(12, len(self.page_numbers))
        for _0 in self.page_numbers:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='previous_page_number', type=12, id=None)
        self.previous_page_number.write(oprot)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
