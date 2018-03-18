from collections import OrderedDict
from itertools import filterfalse
import builtins
import pastpy.gen.online.online_image


class OnlineObjectDetail(object):
    class Builder(object):
        def __init__(
            self,
            attributes=None,
            guid=None,
            id=None,  # @ReservedAssignment
            related_photos=None,
        ):
            '''
            :type attributes: dict(str: str)
            :type guid: str
            :type id: str
            :type related_photos: tuple(pastpy.gen.online.online_image.OnlineImage)
            '''

            self.__attributes = attributes
            self.__guid = guid
            self.__id = id
            self.__related_photos = related_photos

        def build(self):
            return OnlineObjectDetail(attributes=self.__attributes, guid=self.__guid, id=self.__id, related_photos=self.__related_photos)

        @property
        def attributes(self):
            '''
            :rtype: dict(str: str)
            '''

            return self.__attributes.copy() if self.__attributes is not None else None

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.online.online_object_detail.OnlineObjectDetail
            :rtype: pastpy.gen.online.online_object_detail.OnlineObjectDetail
            '''

            builder = cls()
            builder.attributes = template.attributes
            builder.guid = template.guid
            builder.id = template.id
            builder.related_photos = template.related_photos
            return builder

        @property
        def guid(self):
            '''
            :rtype: str
            '''

            return self.__guid

        @property
        def id(self):  # @ReservedAssignment
            '''
            :rtype: str
            '''

            return self.__id

        @property
        def related_photos(self):
            '''
            :rtype: tuple(pastpy.gen.online.online_image.OnlineImage)
            '''

            return self.__related_photos

        def set_attributes(self, attributes):
            '''
            :type attributes: dict(str: str)
            '''

            if attributes is None:
                raise ValueError('attributes is required')
            if not (isinstance(attributes, dict) and len(list(filterfalse(lambda __item: isinstance(__item[0], str) and isinstance(__item[1], str), attributes.items()))) == 0):
                raise TypeError("expected attributes to be a dict(str: str) but it is a %s" % builtins.type(attributes))
            self.__attributes = attributes
            return self

        def set_guid(self, guid):
            '''
            :type guid: str
            '''

            if guid is None:
                raise ValueError('guid is required')
            if not isinstance(guid, str):
                raise TypeError("expected guid to be a str but it is a %s" % builtins.type(guid))
            if guid.isspace():
                raise ValueError("expected guid not to be blank")
            if len(guid) < 1:
                raise ValueError("expected len(guid) to be >= 1, was %d" % len(guid))
            self.__guid = guid
            return self

        def set_id(self, id):  # @ReservedAssignment
            '''
            :type id: str
            '''

            if id is None:
                raise ValueError('id is required')
            if not isinstance(id, str):
                raise TypeError("expected id to be a str but it is a %s" % builtins.type(id))
            if id.isspace():
                raise ValueError("expected id not to be blank")
            if len(id) < 1:
                raise ValueError("expected len(id) to be >= 1, was %d" % len(id))
            self.__id = id
            return self

        def set_related_photos(self, related_photos):
            '''
            :type related_photos: tuple(pastpy.gen.online.online_image.OnlineImage)
            '''

            if related_photos is None:
                raise ValueError('related_photos is required')
            if not (isinstance(related_photos, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.online.online_image.OnlineImage), related_photos))) == 0):
                raise TypeError("expected related_photos to be a tuple(pastpy.gen.online.online_image.OnlineImage) but it is a %s" % builtins.type(related_photos))
            self.__related_photos = related_photos
            return self

        def update(self, online_object_detail):
            '''
            :type attributes: dict(str: str)
            :type guid: str
            :type id: str
            :type related_photos: tuple(pastpy.gen.online.online_image.OnlineImage)
            '''

            if isinstance(online_object_detail, OnlineObjectDetail):
                self.set_attributes(online_object_detail.attributes)
                self.set_guid(online_object_detail.guid)
                self.set_id(online_object_detail.id)
                self.set_related_photos(online_object_detail.related_photos)
            elif isinstance(online_object_detail, dict):
                for key, value in online_object_detail.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(online_object_detail)
            return self

        @attributes.setter
        def attributes(self, attributes):
            '''
            :type attributes: dict(str: str)
            '''

            self.set_attributes(attributes)

        @guid.setter
        def guid(self, guid):
            '''
            :type guid: str
            '''

            self.set_guid(guid)

        @id.setter
        def id(self, id):  # @ReservedAssignment
            '''
            :type id: str
            '''

            self.set_id(id)

        @related_photos.setter
        def related_photos(self, related_photos):
            '''
            :type related_photos: tuple(pastpy.gen.online.online_image.OnlineImage)
            '''

            self.set_related_photos(related_photos)

    class FieldMetadata(object):
        ATTRIBUTES = None
        GUID = None
        ID = None
        RELATED_PHOTOS = None

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
            return (cls.ATTRIBUTES, cls.GUID, cls.ID, cls.RELATED_PHOTOS,)

    FieldMetadata.ATTRIBUTES = FieldMetadata('attributes', dict, None)
    FieldMetadata.GUID = FieldMetadata('guid', str, OrderedDict([('blank', False), ('minLength', 1)]))
    FieldMetadata.ID = FieldMetadata('id', str, OrderedDict([('blank', False), ('minLength', 1)]))
    FieldMetadata.RELATED_PHOTOS = FieldMetadata('related_photos', tuple, None)

    def __init__(
        self,
        attributes,
        guid,
        id,  # @ReservedAssignment
        related_photos,
    ):
        '''
        :type attributes: dict(str: str)
        :type guid: str
        :type id: str
        :type related_photos: tuple(pastpy.gen.online.online_image.OnlineImage)
        '''

        if attributes is None:
            raise ValueError('attributes is required')
        if not (isinstance(attributes, dict) and len(list(filterfalse(lambda __item: isinstance(__item[0], str) and isinstance(__item[1], str), attributes.items()))) == 0):
            raise TypeError("expected attributes to be a dict(str: str) but it is a %s" % builtins.type(attributes))
        self.__attributes = attributes.copy() if attributes is not None else None

        if guid is None:
            raise ValueError('guid is required')
        if not isinstance(guid, str):
            raise TypeError("expected guid to be a str but it is a %s" % builtins.type(guid))
        if guid.isspace():
            raise ValueError("expected guid not to be blank")
        if len(guid) < 1:
            raise ValueError("expected len(guid) to be >= 1, was %d" % len(guid))
        self.__guid = guid

        if id is None:
            raise ValueError('id is required')
        if not isinstance(id, str):
            raise TypeError("expected id to be a str but it is a %s" % builtins.type(id))
        if id.isspace():
            raise ValueError("expected id not to be blank")
        if len(id) < 1:
            raise ValueError("expected len(id) to be >= 1, was %d" % len(id))
        self.__id = id

        if related_photos is None:
            raise ValueError('related_photos is required')
        if not (isinstance(related_photos, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.online.online_image.OnlineImage), related_photos))) == 0):
            raise TypeError("expected related_photos to be a tuple(pastpy.gen.online.online_image.OnlineImage) but it is a %s" % builtins.type(related_photos))
        self.__related_photos = related_photos

    def __eq__(self, other):
        if self.attributes != other.attributes:
            return False
        if self.guid != other.guid:
            return False
        if self.id != other.id:
            return False
        if self.related_photos != other.related_photos:
            return False
        return True

    def __hash__(self):
        return hash((self.attributes, self.guid, self.id, self.related_photos,))

    def __iter__(self):
        return iter((self.attributes, self.guid, self.id, self.related_photos,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('attributes=' + repr(self.attributes))
        field_reprs.append('guid=' + "'" + self.guid.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('id=' + "'" + self.id.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('related_photos=' + repr(self.related_photos))
        return 'OnlineObjectDetail(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('attributes=' + repr(self.attributes))
        field_reprs.append('guid=' + "'" + self.guid.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('id=' + "'" + self.id.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('related_photos=' + repr(self.related_photos))
        return 'OnlineObjectDetail(' + ', '.join(field_reprs) + ')'

    @property
    def attributes(self):
        '''
        :rtype: dict(str: str)
        '''

        return self.__attributes.copy() if self.__attributes is not None else None

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def guid(self):
        '''
        :rtype: str
        '''

        return self.__guid

    @property
    def id(self):  # @ReservedAssignment
        '''
        :rtype: str
        '''

        return self.__id

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.online.online_object_detail.OnlineObjectDetail
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'attributes':
                init_kwds['attributes'] = dict([(iprot.read_string(), iprot.read_string()) for _ in xrange(iprot.read_map_begin()[2])] + (iprot.read_map_end() is None and []))
            elif ifield_name == 'guid':
                init_kwds['guid'] = iprot.read_string()
            elif ifield_name == 'id':
                init_kwds['id'] = iprot.read_string()
            elif ifield_name == 'related_photos':
                init_kwds['related_photos'] = tuple([pastpy.gen.online.online_image.OnlineImage.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    @property
    def related_photos(self):
        '''
        :rtype: tuple(pastpy.gen.online.online_image.OnlineImage)
        '''

        return self.__related_photos

    def replacer(self):
        return cls.Builder.from_template(template=self)

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.online.online_object_detail.OnlineObjectDetail
        '''

        oprot.write_struct_begin('OnlineObjectDetail')

        oprot.write_field_begin(name='attributes', type=13, id=None)
        oprot.write_map_begin(11, len(self.attributes), 11)
        for __key0, __value0 in self.attributes.items():
            oprot.write_string(__key0)
            oprot.write_string(__value0)
        oprot.write_map_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='guid', type=11, id=None)
        oprot.write_string(self.guid)
        oprot.write_field_end()

        oprot.write_field_begin(name='id', type=11, id=None)
        oprot.write_string(self.id)
        oprot.write_field_end()

        oprot.write_field_begin(name='related_photos', type=15, id=None)
        oprot.write_list_begin(12, len(self.related_photos))
        for _0 in self.related_photos:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self