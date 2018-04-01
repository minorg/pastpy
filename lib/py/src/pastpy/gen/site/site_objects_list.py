from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_metadata
import pastpy.gen.site.site_object
import pastpy.gen.site.site_objects_list_page_number


class SiteObjectsList(object):
    class Builder(object):
        def __init__(
            self,
            absolute_href=None,
            metadata=None,
            next_page_number=None,
            objects=None,
            previous_page_number=None,
            visible_page_numbers=None,
        ):
            '''
            :type absolute_href: str
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type visible_page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            self.__absolute_href = absolute_href
            self.__metadata = metadata
            self.__next_page_number = next_page_number
            self.__objects = objects
            self.__previous_page_number = previous_page_number
            self.__visible_page_numbers = visible_page_numbers

        def build(self):
            return SiteObjectsList(absolute_href=self.__absolute_href, metadata=self.__metadata, next_page_number=self.__next_page_number, objects=self.__objects, previous_page_number=self.__previous_page_number, visible_page_numbers=self.__visible_page_numbers)

        @property
        def absolute_href(self):
            '''
            :rtype: str
            '''

            return self.__absolute_href

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_objects_list.SiteObjectsList
            :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
            '''

            builder = cls()
            builder.absolute_href = template.absolute_href
            builder.metadata = template.metadata
            builder.next_page_number = template.next_page_number
            builder.objects = template.objects
            builder.previous_page_number = template.previous_page_number
            builder.visible_page_numbers = template.visible_page_numbers
            return builder

        @property
        def metadata(self):
            '''
            :rtype: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            return self.__metadata

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

        def set_metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            if metadata is None:
                raise ValueError('metadata is required')
            if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
                raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
            self.__metadata = metadata
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

        def set_visible_page_numbers(self, visible_page_numbers):
            '''
            :type visible_page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            if visible_page_numbers is None:
                raise ValueError('visible_page_numbers is required')
            if not (isinstance(visible_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber), visible_page_numbers))) == 0):
                raise TypeError("expected visible_page_numbers to be a tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber) but it is a %s" % builtins.type(visible_page_numbers))
            self.__visible_page_numbers = visible_page_numbers
            return self

        def update(self, site_objects_list):
            '''
            :type absolute_href: str
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            :type visible_page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            if isinstance(site_objects_list, SiteObjectsList):
                self.set_absolute_href(site_objects_list.absolute_href)
                self.set_metadata(site_objects_list.metadata)
                self.set_next_page_number(site_objects_list.next_page_number)
                self.set_objects(site_objects_list.objects)
                self.set_previous_page_number(site_objects_list.previous_page_number)
                self.set_visible_page_numbers(site_objects_list.visible_page_numbers)
            elif isinstance(site_objects_list, dict):
                for key, value in site_objects_list.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_objects_list)
            return self

        @property
        def visible_page_numbers(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            return self.__visible_page_numbers

        @absolute_href.setter
        def absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            self.set_absolute_href(absolute_href)

        @metadata.setter
        def metadata(self, metadata):
            '''
            :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
            '''

            self.set_metadata(metadata)

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

        @previous_page_number.setter
        def previous_page_number(self, previous_page_number):
            '''
            :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
            '''

            self.set_previous_page_number(previous_page_number)

        @visible_page_numbers.setter
        def visible_page_numbers(self, visible_page_numbers):
            '''
            :type visible_page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
            '''

            self.set_visible_page_numbers(visible_page_numbers)

    class FieldMetadata(object):
        ABSOLUTE_HREF = None
        METADATA = None
        NEXT_PAGE_NUMBER = None
        OBJECTS = None
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
            return (cls.ABSOLUTE_HREF, cls.METADATA, cls.NEXT_PAGE_NUMBER, cls.OBJECTS, cls.PREVIOUS_PAGE_NUMBER, cls.VISIBLE_PAGE_NUMBERS,)

    FieldMetadata.ABSOLUTE_HREF = FieldMetadata('absolute_href', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.METADATA = FieldMetadata('metadata', pastpy.gen.site.site_metadata.SiteMetadata, None)
    FieldMetadata.NEXT_PAGE_NUMBER = FieldMetadata('next_page_number', pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', tuple, None)
    FieldMetadata.PREVIOUS_PAGE_NUMBER = FieldMetadata('previous_page_number', pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber, None)
    FieldMetadata.VISIBLE_PAGE_NUMBERS = FieldMetadata('visible_page_numbers', tuple, None)

    def __init__(
        self,
        absolute_href,
        metadata,
        next_page_number,
        objects,
        previous_page_number,
        visible_page_numbers,
    ):
        '''
        :type absolute_href: str
        :type metadata: pastpy.gen.site.site_metadata.SiteMetadata
        :type next_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        :type objects: tuple(pastpy.gen.site.site_object.SiteObject)
        :type previous_page_number: pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber
        :type visible_page_numbers: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
        '''

        if absolute_href is None:
            raise ValueError('absolute_href is required')
        if not isinstance(absolute_href, str):
            raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
        self.__absolute_href = absolute_href

        if metadata is None:
            raise ValueError('metadata is required')
        if not isinstance(metadata, pastpy.gen.site.site_metadata.SiteMetadata):
            raise TypeError("expected metadata to be a pastpy.gen.site.site_metadata.SiteMetadata but it is a %s" % builtins.type(metadata))
        self.__metadata = metadata

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

        if previous_page_number is None:
            raise ValueError('previous_page_number is required')
        if not isinstance(previous_page_number, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber):
            raise TypeError("expected previous_page_number to be a pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber but it is a %s" % builtins.type(previous_page_number))
        self.__previous_page_number = previous_page_number

        if visible_page_numbers is None:
            raise ValueError('visible_page_numbers is required')
        if not (isinstance(visible_page_numbers, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber), visible_page_numbers))) == 0):
            raise TypeError("expected visible_page_numbers to be a tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber) but it is a %s" % builtins.type(visible_page_numbers))
        self.__visible_page_numbers = visible_page_numbers

    def __eq__(self, other):
        if self.absolute_href != other.absolute_href:
            return False
        if self.metadata != other.metadata:
            return False
        if self.next_page_number != other.next_page_number:
            return False
        if self.objects != other.objects:
            return False
        if self.previous_page_number != other.previous_page_number:
            return False
        if self.visible_page_numbers != other.visible_page_numbers:
            return False
        return True

    def __hash__(self):
        return hash((self.absolute_href, self.metadata, self.next_page_number, self.objects, self.previous_page_number, self.visible_page_numbers,))

    def __iter__(self):
        return iter((self.absolute_href, self.metadata, self.next_page_number, self.objects, self.previous_page_number, self.visible_page_numbers,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        field_reprs.append('visible_page_numbers=' + repr(self.visible_page_numbers))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('metadata=' + repr(self.metadata))
        field_reprs.append('next_page_number=' + repr(self.next_page_number))
        field_reprs.append('objects=' + repr(self.objects))
        field_reprs.append('previous_page_number=' + repr(self.previous_page_number))
        field_reprs.append('visible_page_numbers=' + repr(self.visible_page_numbers))
        return 'SiteObjectsList(' + ', '.join(field_reprs) + ')'

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

        metadata = _dict.get("metadata")
        if metadata is None:
            raise KeyError("metadata")
        metadata = pastpy.gen.site.site_metadata.SiteMetadata.from_builtins(metadata)
        __builder.metadata = metadata

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

        previous_page_number = _dict.get("previous_page_number")
        if previous_page_number is None:
            raise KeyError("previous_page_number")
        previous_page_number = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.from_builtins(previous_page_number)
        __builder.previous_page_number = previous_page_number

        visible_page_numbers = _dict.get("visible_page_numbers")
        if visible_page_numbers is None:
            raise KeyError("visible_page_numbers")
        visible_page_numbers = tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.from_builtins(element0) for element0 in visible_page_numbers)
        __builder.visible_page_numbers = visible_page_numbers

        return __builder.build()

    @property
    def metadata(self):
        '''
        :rtype: pastpy.gen.site.site_metadata.SiteMetadata
        '''

        return self.__metadata

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
        :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'absolute_href':
                init_kwds['absolute_href'] = iprot.read_string()
            elif ifield_name == 'metadata':
                init_kwds['metadata'] = pastpy.gen.site.site_metadata.SiteMetadata.read(iprot)
            elif ifield_name == 'next_page_number':
                init_kwds['next_page_number'] = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot)
            elif ifield_name == 'objects':
                init_kwds['objects'] = tuple([pastpy.gen.site.site_object.SiteObject.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'previous_page_number':
                init_kwds['previous_page_number'] = pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot)
            elif ifield_name == 'visible_page_numbers':
                init_kwds['visible_page_numbers'] = tuple([pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["absolute_href"] = self.absolute_href
        dict_["metadata"] = self.metadata.to_builtins()
        dict_["next_page_number"] = self.next_page_number.to_builtins()
        dict_["objects"] = tuple(element0.to_builtins() for element0 in self.objects)
        dict_["previous_page_number"] = self.previous_page_number.to_builtins()
        dict_["visible_page_numbers"] = tuple(element0.to_builtins() for element0 in self.visible_page_numbers)
        return dict_

    @property
    def visible_page_numbers(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_objects_list_page_number.SiteObjectsListPageNumber)
        '''

        return self.__visible_page_numbers

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_objects_list.SiteObjectsList
        '''

        oprot.write_struct_begin('SiteObjectsList')

        oprot.write_field_begin(name='absolute_href', type=11, id=None)
        oprot.write_string(self.absolute_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='metadata', type=12, id=None)
        self.metadata.write(oprot)
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
