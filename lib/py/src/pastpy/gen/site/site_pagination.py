from itertools import filterfalse
import builtins
import pastpy.gen.site.site_pagination_page_number


class SitePagination(object):
    class Builder(object):
        def __init__(
            self,
            next_page_number=None,
            previous_page_number=None,
            visible_page_numbers=None,
        ):
            '''
            :type next_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            :type previous_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            :type visible_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            self.__next_page_number = next_page_number
            self.__previous_page_number = previous_page_number
            self.__visible_page_numbers = visible_page_numbers

        def build(self):
            return SitePagination(next_page_number=self.__next_page_number, previous_page_number=self.__previous_page_number, visible_page_numbers=self.__visible_page_numbers)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_pagination.SitePagination
            :rtype: pastpy.gen.site.site_pagination.SitePagination
            '''

            builder = cls()
            builder.next_page_number = template.next_page_number
            builder.previous_page_number = template.previous_page_number
            builder.visible_page_numbers = template.visible_page_numbers
            return builder

        @property
        def next_page_number(self):
            '''
            :rtype: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            return self.__next_page_number

        @property
        def previous_page_number(self):
            '''
            :rtype: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            return self.__previous_page_number

        def set_next_page_number(self, next_page_number):
            '''
            :type next_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            if next_page_number is None:
                raise ValueError('next_page_number is required')
            if not isinstance(next_page_number, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber):
                raise TypeError("expected next_page_number to be a pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber but it is a %s" % builtins.type(next_page_number))
            self.__next_page_number = next_page_number
            return self

        def set_previous_page_number(self, previous_page_number):
            '''
            :type previous_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            if previous_page_number is None:
                raise ValueError('previous_page_number is required')
            if not isinstance(previous_page_number, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber):
                raise TypeError("expected previous_page_number to be a pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber but it is a %s" % builtins.type(previous_page_number))
            self.__previous_page_number = previous_page_number
            return self

        def set_visible_page_numbers(self, visible_page_numbers):
            '''
            :type visible_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            if visible_page_numbers is None:
                raise ValueError('visible_page_numbers is required')
            if not (isinstance(visible_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber), visible_page_numbers))) == 0):
                raise TypeError("expected visible_page_numbers to be a tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber) but it is a %s" % builtins.type(visible_page_numbers))
            self.__visible_page_numbers = visible_page_numbers
            return self

        def update(self, site_pagination):
            '''
            :type next_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            :type previous_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            :type visible_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            if isinstance(site_pagination, SitePagination):
                self.set_next_page_number(site_pagination.next_page_number)
                self.set_previous_page_number(site_pagination.previous_page_number)
                self.set_visible_page_numbers(site_pagination.visible_page_numbers)
            elif isinstance(site_pagination, dict):
                for key, value in site_pagination.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_pagination)
            return self

        @property
        def visible_page_numbers(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            return self.__visible_page_numbers

        @next_page_number.setter
        def next_page_number(self, next_page_number):
            '''
            :type next_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            self.set_next_page_number(next_page_number)

        @previous_page_number.setter
        def previous_page_number(self, previous_page_number):
            '''
            :type previous_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
            '''

            self.set_previous_page_number(previous_page_number)

        @visible_page_numbers.setter
        def visible_page_numbers(self, visible_page_numbers):
            '''
            :type visible_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
            '''

            self.set_visible_page_numbers(visible_page_numbers)

    class FieldMetadata(object):
        NEXT_PAGE_NUMBER = None
        PREVIOUS_PAGE_NUMBER = None
        VISIBLE_PAGE_NUMBERS = None

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
            return (cls.NEXT_PAGE_NUMBER, cls.PREVIOUS_PAGE_NUMBER, cls.VISIBLE_PAGE_NUMBERS,)

    FieldMetadata.NEXT_PAGE_NUMBER = FieldMetadata('next_page_number', pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber, None)
    FieldMetadata.PREVIOUS_PAGE_NUMBER = FieldMetadata('previous_page_number', pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber, None)
    FieldMetadata.VISIBLE_PAGE_NUMBERS = FieldMetadata('visible_page_numbers', tuple, None)

    def __init__(
        self,
        next_page_number,
        previous_page_number,
        visible_page_numbers,
    ):
        '''
        :type next_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
        :type previous_page_number: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
        :type visible_page_numbers: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
        '''

        if next_page_number is None:
            raise ValueError('next_page_number is required')
        if not isinstance(next_page_number, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber):
            raise TypeError("expected next_page_number to be a pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber but it is a %s" % builtins.type(next_page_number))
        self.__next_page_number = next_page_number

        if previous_page_number is None:
            raise ValueError('previous_page_number is required')
        if not isinstance(previous_page_number, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber):
            raise TypeError("expected previous_page_number to be a pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber but it is a %s" % builtins.type(previous_page_number))
        self.__previous_page_number = previous_page_number

        if visible_page_numbers is None:
            raise ValueError('visible_page_numbers is required')
        if not (isinstance(visible_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber), visible_page_numbers))) == 0):
            raise TypeError("expected visible_page_numbers to be a tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber) but it is a %s" % builtins.type(visible_page_numbers))
        self.__visible_page_numbers = visible_page_numbers

    def __eq__(self, other):
        if self.next_page_number != other.next_page_number:
            return False
        if self.previous_page_number != other.previous_page_number:
            return False
        if self.visible_page_numbers != other.visible_page_numbers:
            return False
        return True

    def __hash__(self):
        return hash((self.next_page_number, self.previous_page_number, self.visible_page_numbers,))

    def __iter__(self):
        return iter((self.next_page_number, self.previous_page_number, self.visible_page_numbers,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        field_reprs.append('visible_page_numbers=' + repr(self.visible_page_numbers))
        return 'SitePagination(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        field_reprs.append('visible_page_numbers=' + repr(self.visible_page_numbers))
        return 'SitePagination(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        next_page_number = _dict.get("next_page_number")
        if next_page_number is None:
            raise KeyError("next_page_number")
        next_page_number = pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.from_builtins(next_page_number)
        __builder.next_page_number = next_page_number

        previous_page_number = _dict.get("previous_page_number")
        if previous_page_number is None:
            raise KeyError("previous_page_number")
        previous_page_number = pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.from_builtins(previous_page_number)
        __builder.previous_page_number = previous_page_number

        visible_page_numbers = _dict.get("visible_page_numbers")
        if visible_page_numbers is None:
            raise KeyError("visible_page_numbers")
        visible_page_numbers = tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.from_builtins(element0) for element0 in visible_page_numbers)
        __builder.visible_page_numbers = visible_page_numbers

        return __builder.build()

    @property
    def next_page_number(self):
        '''
        :rtype: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
        '''

        return self.__next_page_number

    @property
    def previous_page_number(self):
        '''
        :rtype: pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber
        '''

        return self.__previous_page_number

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_pagination.SitePagination
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'next_page_number':
                init_kwds['next_page_number'] = pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.read(iprot)
            elif ifield_name == 'previous_page_number':
                init_kwds['previous_page_number'] = pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.read(iprot)
            elif ifield_name == 'visible_page_numbers':
                init_kwds['visible_page_numbers'] = tuple([pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["next_page_number"] = self.next_page_number.to_builtins()
        dict_["previous_page_number"] = self.previous_page_number.to_builtins()
        dict_["visible_page_numbers"] = tuple(element0.to_builtins() for element0 in self.visible_page_numbers)
        return dict_

    @property
    def visible_page_numbers(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_pagination_page_number.SitePaginationPageNumber)
        '''

        return self.__visible_page_numbers

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_pagination.SitePagination
        '''

        oprot.write_struct_begin('SitePagination')

        oprot.write_field_begin(name='next_page_number', type=12, id=None)
        self.next_page_number.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='previous_page_number', type=12, id=None)
        self.previous_page_number.write(oprot)
        oprot.write_field_end()

        oprot.write_field_begin(name='visible_page_numbers', type=15, id=None)
        oprot.write_list_begin(12, len(self.visible_page_numbers))
        for _0 in self.visible_page_numbers:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
