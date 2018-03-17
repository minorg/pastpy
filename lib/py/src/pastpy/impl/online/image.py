from collections import OrderedDict
import builtins


class Image(object):
    class Builder(object):
        def __init__(
            self,
            full_size_url=None,
            thumbnail_url=None,
            title=None,
        ):
            '''
            :type full_size_url: str
            :type thumbnail_url: str
            :type title: str
            '''

            self.__full_size_url = full_size_url
            self.__thumbnail_url = thumbnail_url
            self.__title = title

        def build(self):
            return Image(full_size_url=self.__full_size_url, thumbnail_url=self.__thumbnail_url, title=self.__title)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.impl.online.image.Image
            :rtype: pastpy.impl.online.image.Image
            '''

            builder = cls()
            builder.full_size_url = full_size_url
            builder.thumbnail_url = thumbnail_url
            builder.title = title
            return builder

        @property
        def full_size_url(self):
            '''
            :rtype: str
            '''

            return self.__full_size_url

        def set_full_size_url(self, full_size_url):
            '''
            :type full_size_url: str
            '''

            if full_size_url is None:
                raise ValueError('full_size_url is required')
            if not isinstance(full_size_url, str):
                raise TypeError("expected full_size_url to be a str but it is a %s" % builtins.type(full_size_url))
            self.__full_size_url = full_size_url
            return self

        def set_thumbnail_url(self, thumbnail_url):
            '''
            :type thumbnail_url: str
            '''

            if thumbnail_url is None:
                raise ValueError('thumbnail_url is required')
            if not isinstance(thumbnail_url, str):
                raise TypeError("expected thumbnail_url to be a str but it is a %s" % builtins.type(thumbnail_url))
            self.__thumbnail_url = thumbnail_url
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
        def thumbnail_url(self):
            '''
            :rtype: str
            '''

            return self.__thumbnail_url

        @property
        def title(self):
            '''
            :rtype: str
            '''

            return self.__title

        def update(self, image):
            '''
            :type full_size_url: str
            :type thumbnail_url: str
            :type title: str
            '''

            if isinstance(image, Image):
                self.set_full_size_url(image.full_size_url)
                self.set_thumbnail_url(image.thumbnail_url)
                self.set_title(image.title)
            elif isinstance(image, dict):
                for key, value in image.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(image)
            return self

        @full_size_url.setter
        def full_size_url(self, full_size_url):
            '''
            :type full_size_url: str
            '''

            self.set_full_size_url(full_size_url)

        @thumbnail_url.setter
        def thumbnail_url(self, thumbnail_url):
            '''
            :type thumbnail_url: str
            '''

            self.set_thumbnail_url(thumbnail_url)

        @title.setter
        def title(self, title):
            '''
            :type title: str
            '''

            self.set_title(title)

    class FieldMetadata(object):
        FULL_SIZE_URL = None
        THUMBNAIL_URL = None
        TITLE = None

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
            return (cls.FULL_SIZE_URL, cls.THUMBNAIL_URL, cls.TITLE,)

    FieldMetadata.FULL_SIZE_URL = FieldMetadata('full_size_url', str, None)
    FieldMetadata.THUMBNAIL_URL = FieldMetadata('thumbnail_url', str, None)
    FieldMetadata.TITLE = FieldMetadata('title', str, OrderedDict([('blank', False), ('minLength', 1)]))

    def __init__(
        self,
        full_size_url,
        thumbnail_url,
        title,
    ):
        '''
        :type full_size_url: str
        :type thumbnail_url: str
        :type title: str
        '''

        if full_size_url is None:
            raise ValueError('full_size_url is required')
        if not isinstance(full_size_url, str):
            raise TypeError("expected full_size_url to be a str but it is a %s" % builtins.type(full_size_url))
        self.__full_size_url = full_size_url

        if thumbnail_url is None:
            raise ValueError('thumbnail_url is required')
        if not isinstance(thumbnail_url, str):
            raise TypeError("expected thumbnail_url to be a str but it is a %s" % builtins.type(thumbnail_url))
        self.__thumbnail_url = thumbnail_url

        if title is None:
            raise ValueError('title is required')
        if not isinstance(title, str):
            raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
        if title.isspace():
            raise ValueError("expected title not to be blank")
        if len(title) < 1:
            raise ValueError("expected len(title) to be >= 1, was %d" % len(title))
        self.__title = title

    def __eq__(self, other):
        if self.full_size_url != other.full_size_url:
            return False
        if self.thumbnail_url != other.thumbnail_url:
            return False
        if self.title != other.title:
            return False
        return True

    def __hash__(self):
        return hash((self.full_size_url, self.thumbnail_url, self.title,))

    def __iter__(self):
        return iter((self.full_size_url, self.thumbnail_url, self.title,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('full_size_url=' + "'" + self.full_size_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'Image(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('full_size_url=' + "'" + self.full_size_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'Image(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def full_size_url(self):
        '''
        :rtype: str
        '''

        return self.__full_size_url

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.impl.online.image.Image
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'full_size_url':
                init_kwds['full_size_url'] = iprot.read_string()
            elif ifield_name == 'thumbnail_url':
                init_kwds['thumbnail_url'] = iprot.read_string()
            elif ifield_name == 'title':
                init_kwds['title'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return cls.Builder.from_template(template=self)

    @property
    def thumbnail_url(self):
        '''
        :rtype: str
        '''

        return self.__thumbnail_url

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
        :rtype: pastpy.impl.online.image.Image
        '''

        oprot.write_struct_begin('Image')

        oprot.write_field_begin(name='full_size_url', type=11, id=None)
        oprot.write_string(self.full_size_url)
        oprot.write_field_end()

        oprot.write_field_begin(name='thumbnail_url', type=11, id=None)
        oprot.write_string(self.thumbnail_url)
        oprot.write_field_end()

        oprot.write_field_begin(name='title', type=11, id=None)
        oprot.write_string(self.title)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
