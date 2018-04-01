import builtins
import pastpy.gen.non_blank_string


class SiteImage(object):
    class Builder(object):
        def __init__(
            self,
            full_size_url=None,
            thumbnail_url=None,
            title=None,
        ):
            '''
            :type full_size_url: str or None
            :type thumbnail_url: str or None
            :type title: str or None
            '''

            self.__full_size_url = full_size_url
            self.__thumbnail_url = thumbnail_url
            self.__title = title

        def build(self):
            return SiteImage(full_size_url=self.__full_size_url, thumbnail_url=self.__thumbnail_url, title=self.__title)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_image.SiteImage
            :rtype: pastpy.gen.site.site_image.SiteImage
            '''

            builder = cls()
            builder.full_size_url = template.full_size_url
            builder.thumbnail_url = template.thumbnail_url
            builder.title = template.title
            return builder

        @property
        def full_size_url(self):
            '''
            :rtype: str
            '''

            return self.__full_size_url

        def set_full_size_url(self, full_size_url):
            '''
            :type full_size_url: str or None
            '''

            if full_size_url is not None:
                if not isinstance(full_size_url, str):
                    raise TypeError("expected full_size_url to be a str but it is a %s" % builtins.type(full_size_url))
            self.__full_size_url = full_size_url
            return self

        def set_thumbnail_url(self, thumbnail_url):
            '''
            :type thumbnail_url: str or None
            '''

            if thumbnail_url is not None:
                if not isinstance(thumbnail_url, str):
                    raise TypeError("expected thumbnail_url to be a str but it is a %s" % builtins.type(thumbnail_url))
            self.__thumbnail_url = thumbnail_url
            return self

        def set_title(self, title):
            '''
            :type title: str or None
            '''

            if title is not None:
                if not isinstance(title, str):
                    raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
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

        def update(self, site_image):
            '''
            :type full_size_url: str or None
            :type thumbnail_url: str or None
            :type title: str or None
            '''

            if isinstance(site_image, SiteImage):
                self.set_full_size_url(site_image.full_size_url)
                self.set_thumbnail_url(site_image.thumbnail_url)
                self.set_title(site_image.title)
            elif isinstance(site_image, dict):
                for key, value in site_image.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_image)
            return self

        @full_size_url.setter
        def full_size_url(self, full_size_url):
            '''
            :type full_size_url: str or None
            '''

            self.set_full_size_url(full_size_url)

        @thumbnail_url.setter
        def thumbnail_url(self, thumbnail_url):
            '''
            :type thumbnail_url: str or None
            '''

            self.set_thumbnail_url(thumbnail_url)

        @title.setter
        def title(self, title):
            '''
            :type title: str or None
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
    FieldMetadata.TITLE = FieldMetadata('title', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        full_size_url=None,
        thumbnail_url=None,
        title=None,
    ):
        '''
        :type full_size_url: str or None
        :type thumbnail_url: str or None
        :type title: str or None
        '''

        if full_size_url is not None:
            if not isinstance(full_size_url, str):
                raise TypeError("expected full_size_url to be a str but it is a %s" % builtins.type(full_size_url))
        self.__full_size_url = full_size_url

        if thumbnail_url is not None:
            if not isinstance(thumbnail_url, str):
                raise TypeError("expected thumbnail_url to be a str but it is a %s" % builtins.type(thumbnail_url))
        self.__thumbnail_url = thumbnail_url

        if title is not None:
            if not isinstance(title, str):
                raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
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
        if self.full_size_url is not None:
            field_reprs.append('full_size_url=' + "'" + self.full_size_url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail_url is not None:
            field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.title is not None:
            field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteImage(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.full_size_url is not None:
            field_reprs.append('full_size_url=' + "'" + self.full_size_url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.thumbnail_url is not None:
            field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        if self.title is not None:
            field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteImage(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        __builder.full_size_url = _dict.get("full_size_url")

        __builder.thumbnail_url = _dict.get("thumbnail_url")

        __builder.title = _dict.get("title")

        return __builder.build()

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
        :rtype: pastpy.gen.site.site_image.SiteImage
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'full_size_url':
                try:
                    init_kwds['full_size_url'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'thumbnail_url':
                try:
                    init_kwds['thumbnail_url'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'title':
                try:
                    init_kwds['title'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

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

    def to_builtins(self):
        dict_ = {}
        dict_["full_size_url"] = self.full_size_url
        dict_["thumbnail_url"] = self.thumbnail_url
        dict_["title"] = self.title
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_image.SiteImage
        '''

        oprot.write_struct_begin('SiteImage')

        if self.full_size_url is not None:
            oprot.write_field_begin(name='full_size_url', type=11, id=None)
            oprot.write_string(self.full_size_url)
            oprot.write_field_end()

        if self.thumbnail_url is not None:
            oprot.write_field_begin(name='thumbnail_url', type=11, id=None)
            oprot.write_string(self.thumbnail_url)
            oprot.write_field_end()

        if self.title is not None:
            oprot.write_field_begin(name='title', type=11, id=None)
            oprot.write_string(self.title)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
