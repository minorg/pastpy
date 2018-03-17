from collections import OrderedDict
from itertools import filterfalse
import builtins
import pastpy.impl.online.image


class ObjectDetail(object):
    class Builder(object):
        def __init__(
            self,
            related_photos=None,
        ):
            '''
            :type related_photos: tuple(pastpy.impl.online.image.Image) or None
            '''

            self.__related_photos = related_photos

        def build(self):
            return ObjectDetail(related_photos=self.__related_photos)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.impl.online.object_detail.ObjectDetail
            :rtype: pastpy.impl.online.object_detail.ObjectDetail
            '''

            builder = cls()
            builder.related_photos = related_photos
            return builder

        @property
        def related_photos(self):
            '''
            :rtype: tuple(pastpy.impl.online.image.Image)
            '''

            return self.__related_photos

        def set_related_photos(self, related_photos):
            '''
            :type related_photos: tuple(pastpy.impl.online.image.Image) or None
            '''

            if related_photos is not None:
                if not (isinstance(related_photos, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.impl.online.image.Image), related_photos))) == 0):
                    raise TypeError("expected related_photos to be a tuple(pastpy.impl.online.image.Image) but it is a %s" % builtins.type(related_photos))
            self.__related_photos = related_photos
            return self

        def update(self, object_detail):
            '''
            :type related_photos: tuple(pastpy.impl.online.image.Image) or None
            '''

            if isinstance(object_detail, ObjectDetail):
                self.set_related_photos(object_detail.related_photos)
            elif isinstance(object_detail, dict):
                for key, value in object_detail.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(object_detail)
            return self

        @related_photos.setter
        def related_photos(self, related_photos):
            '''
            :type related_photos: tuple(pastpy.impl.online.image.Image) or None
            '''

            self.set_related_photos(related_photos)

    class FieldMetadata(object):
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
            return (cls.RELATED_PHOTOS,)

    FieldMetadata.RELATED_PHOTOS = FieldMetadata('related_photos', tuple, None)

    def __init__(
        self,
        related_photos=None,
    ):
        '''
        :type related_photos: tuple(pastpy.impl.online.image.Image) or None
        '''

        if related_photos is not None:
            if not (isinstance(related_photos, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.impl.online.image.Image), related_photos))) == 0):
                raise TypeError("expected related_photos to be a tuple(pastpy.impl.online.image.Image) but it is a %s" % builtins.type(related_photos))
        self.__related_photos = related_photos

    def __eq__(self, other):
        if self.related_photos != other.related_photos:
            return False
        return True

    def __hash__(self):
        return hash(self.related_photos)

    def __iter__(self):
        return iter((self.related_photos,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        if self.related_photos is not None:
            field_reprs.append('related_photos=' + repr(self.related_photos))
        return 'ObjectDetail(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.related_photos is not None:
            field_reprs.append('related_photos=' + repr(self.related_photos))
        return 'ObjectDetail(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.impl.online.object_detail.ObjectDetail
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'related_photos':
                init_kwds['related_photos'] = tuple([pastpy.impl.online.image.Image.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    @property
    def related_photos(self):
        '''
        :rtype: tuple(pastpy.impl.online.image.Image)
        '''

        return self.__related_photos

    def replacer(self):
        return cls.Builder.from_template(template=self)

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.impl.online.object_detail.ObjectDetail
        '''

        oprot.write_struct_begin('ObjectDetail')

        if self.related_photos is not None:
            oprot.write_field_begin(name='related_photos', type=15, id=None)
            oprot.write_list_begin(12, len(self.related_photos))
            for _0 in self.related_photos:
                _0.write(oprot)
            oprot.write_list_end()
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
