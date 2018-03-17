from collections import OrderedDict
import builtins


class ObjectsListItem(object):
    class Builder(object):
        def __init__(
            self,
            detail_href=None,
            record_type=None,
            title=None,
            thumbnail_src=None,
        ):
            '''
            :type detail_href: str
            :type record_type: str
            :type title: str
            :type thumbnail_src: str or None
            '''

            self.__detail_href = detail_href
            self.__record_type = record_type
            self.__title = title
            self.__thumbnail_src = thumbnail_src

        def build(self):
            return ObjectsListItem(detail_href=self.__detail_href, record_type=self.__record_type, title=self.__title, thumbnail_src=self.__thumbnail_src)

        @property
        def detail_href(self):
            '''
            :rtype: str
            '''

            return self.__detail_href

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.impl.online.objects_list_item.ObjectsListItem
            :rtype: pastpy.impl.online.objects_list_item.ObjectsListItem
            '''

            builder = cls()
            builder.detail_href = detail_href
            builder.record_type = record_type
            builder.title = title
            builder.thumbnail_src = thumbnail_src
            return builder

        @property
        def record_type(self):
            '''
            :rtype: str
            '''

            return self.__record_type

        def set_detail_href(self, detail_href):
            '''
            :type detail_href: str
            '''

            if detail_href is None:
                raise ValueError('detail_href is required')
            if not isinstance(detail_href, str):
                raise TypeError("expected detail_href to be a str but it is a %s" % builtins.type(detail_href))
            if detail_href.isspace():
                raise ValueError("expected detail_href not to be blank")
            if len(detail_href) < 1:
                raise ValueError("expected len(detail_href) to be >= 1, was %d" % len(detail_href))
            self.__detail_href = detail_href
            return self

        def set_record_type(self, record_type):
            '''
            :type record_type: str
            '''

            if record_type is None:
                raise ValueError('record_type is required')
            if not isinstance(record_type, str):
                raise TypeError("expected record_type to be a str but it is a %s" % builtins.type(record_type))
            if record_type.isspace():
                raise ValueError("expected record_type not to be blank")
            if len(record_type) < 1:
                raise ValueError("expected len(record_type) to be >= 1, was %d" % len(record_type))
            self.__record_type = record_type
            return self

        def set_thumbnail_src(self, thumbnail_src):
            '''
            :type thumbnail_src: str or None
            '''

            if thumbnail_src is not None:
                if not isinstance(thumbnail_src, str):
                    raise TypeError("expected thumbnail_src to be a str but it is a %s" % builtins.type(thumbnail_src))
            self.__thumbnail_src = thumbnail_src
            return self

        def set_title(self, title):
            '''
            :type title: str
            '''

            if title is None:
                raise ValueError('title is required')
            if not isinstance(title, str):
                raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
            if title.isspace():
                raise ValueError("expected title not to be blank")
            if len(title) < 1:
                raise ValueError("expected len(title) to be >= 1, was %d" % len(title))
            self.__title = title
            return self

        @property
        def thumbnail_src(self):
            '''
            :rtype: str
            '''

            return self.__thumbnail_src

        @property
        def title(self):
            '''
            :rtype: str
            '''

            return self.__title

        def update(self, objects_list_item):
            '''
            :type detail_href: str
            :type record_type: str
            :type title: str
            :type thumbnail_src: str or None
            '''

            if isinstance(objects_list_item, ObjectsListItem):
                self.set_detail_href(objects_list_item.detail_href)
                self.set_record_type(objects_list_item.record_type)
                self.set_title(objects_list_item.title)
                self.set_thumbnail_src(objects_list_item.thumbnail_src)
            elif isinstance(objects_list_item, dict):
                for key, value in objects_list_item.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(objects_list_item)
            return self

        @detail_href.setter
        def detail_href(self, detail_href):
            '''
            :type detail_href: str
            '''

            self.set_detail_href(detail_href)

        @record_type.setter
        def record_type(self, record_type):
            '''
            :type record_type: str
            '''

            self.set_record_type(record_type)

        @thumbnail_src.setter
        def thumbnail_src(self, thumbnail_src):
            '''
            :type thumbnail_src: str or None
            '''

            self.set_thumbnail_src(thumbnail_src)

        @title.setter
        def title(self, title):
            '''
            :type title: str
            '''

            self.set_title(title)

    class FieldMetadata(object):
        DETAIL_HREF = None
        RECORD_TYPE = None
        TITLE = None
        THUMBNAIL_SRC = None

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
            return (cls.DETAIL_HREF, cls.RECORD_TYPE, cls.TITLE, cls.THUMBNAIL_SRC,)

    FieldMetadata.DETAIL_HREF = FieldMetadata('detail_href', str, OrderedDict([('blank', False), ('minLength', 1)]))
    FieldMetadata.RECORD_TYPE = FieldMetadata('record_type', str, OrderedDict([('blank', False), ('minLength', 1)]))
    FieldMetadata.TITLE = FieldMetadata('title', str, OrderedDict([('blank', False), ('minLength', 1)]))
    FieldMetadata.THUMBNAIL_SRC = FieldMetadata('thumbnail_src', str, None)

    def __init__(
        self,
        detail_href,
        record_type,
        title,
        thumbnail_src=None,
    ):
        '''
        :type detail_href: str
        :type record_type: str
        :type title: str
        :type thumbnail_src: str or None
        '''

        if detail_href is None:
            raise ValueError('detail_href is required')
        if not isinstance(detail_href, str):
            raise TypeError("expected detail_href to be a str but it is a %s" % builtins.type(detail_href))
        if detail_href.isspace():
            raise ValueError("expected detail_href not to be blank")
        if len(detail_href) < 1:
            raise ValueError("expected len(detail_href) to be >= 1, was %d" % len(detail_href))
        self.__detail_href = detail_href

        if record_type is None:
            raise ValueError('record_type is required')
        if not isinstance(record_type, str):
            raise TypeError("expected record_type to be a str but it is a %s" % builtins.type(record_type))
        if record_type.isspace():
            raise ValueError("expected record_type not to be blank")
        if len(record_type) < 1:
            raise ValueError("expected len(record_type) to be >= 1, was %d" % len(record_type))
        self.__record_type = record_type

        if title is None:
            raise ValueError('title is required')
        if not isinstance(title, str):
            raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
        if title.isspace():
            raise ValueError("expected title not to be blank")
        if len(title) < 1:
            raise ValueError("expected len(title) to be >= 1, was %d" % len(title))
        self.__title = title

        if thumbnail_src is not None:
            if not isinstance(thumbnail_src, str):
                raise TypeError("expected thumbnail_src to be a str but it is a %s" % builtins.type(thumbnail_src))
        self.__thumbnail_src = thumbnail_src

    def __eq__(self, other):
        if self.detail_href != other.detail_href:
            return False
        if self.record_type != other.record_type:
            return False
        if self.title != other.title:
            return False
        if self.thumbnail_src != other.thumbnail_src:
            return False
        return True

    def __hash__(self):
        return hash((self.detail_href, self.record_type, self.title, self.thumbnail_src,))

    def __iter__(self):
        return iter((self.detail_href, self.record_type, self.title, self.thumbnail_src,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('detail_href=' + "'" + self.detail_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('record_type=' + "'" + self.record_type.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail_src is not None:
            field_reprs.append('thumbnail_src=' + "'" + self.thumbnail_src.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectsListItem(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('detail_href=' + "'" + self.detail_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('record_type=' + "'" + self.record_type.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail_src is not None:
            field_reprs.append('thumbnail_src=' + "'" + self.thumbnail_src.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectsListItem(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def detail_href(self):
        '''
        :rtype: str
        '''

        return self.__detail_href

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.impl.online.objects_list_item.ObjectsListItem
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'detail_href':
                init_kwds['detail_href'] = iprot.read_string()
            elif ifield_name == 'record_type':
                init_kwds['record_type'] = iprot.read_string()
            elif ifield_name == 'title':
                init_kwds['title'] = iprot.read_string()
            elif ifield_name == 'thumbnail_src':
                try:
                    init_kwds['thumbnail_src'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    @property
    def record_type(self):
        '''
        :rtype: str
        '''

        return self.__record_type

    def replacer(self):
        return cls.Builder.from_template(template=self)

    @property
    def thumbnail_src(self):
        '''
        :rtype: str
        '''

        return self.__thumbnail_src

    @property
    def title(self):
        '''
        :rtype: str
        '''

        return self.__title

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.impl.online.objects_list_item.ObjectsListItem
        '''

        oprot.write_struct_begin('ObjectsListItem')

        oprot.write_field_begin(name='detail_href', type=11, id=None)
        oprot.write_string(self.detail_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='record_type', type=11, id=None)
        oprot.write_string(self.record_type)
        oprot.write_field_end()

        oprot.write_field_begin(name='title', type=11, id=None)
        oprot.write_string(self.title)
        oprot.write_field_end()

        if self.thumbnail_src is not None:
            oprot.write_field_begin(name='thumbnail_src', type=11, id=None)
            oprot.write_string(self.thumbnail_src)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
