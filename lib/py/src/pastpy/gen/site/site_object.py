from itertools import filterfalse
import builtins
import pastpy.gen.non_blank_string
import pastpy.gen.site.site_image
import pastpy.gen.site.site_key_value_pair


class SiteObject(object):
    class Builder(object):
        def __init__(
            self,
            absolute_href=None,
            file_name=None,
            full_size_images=None,
            has_full_size_images=None,
            has_thumbnail_images=None,
            impl_attributes=None,
            name=None,
            standard_attributes=None,
            thumbnail_images=None,
            thumbnail_url=None,
            title=None,
        ):
            '''
            :type absolute_href: str
            :type file_name: str
            :type full_size_images: tuple(pastpy.gen.site.site_image.SiteImage)
            :type has_full_size_images: bool
            :type has_thumbnail_images: bool
            :type impl_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            :type name: str
            :type standard_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            :type thumbnail_images: tuple(pastpy.gen.site.site_image.SiteImage)
            :type thumbnail_url: str
            :type title: str
            '''

            self.__absolute_href = absolute_href
            self.__file_name = file_name
            self.__full_size_images = full_size_images
            self.__has_full_size_images = has_full_size_images
            self.__has_thumbnail_images = has_thumbnail_images
            self.__impl_attributes = impl_attributes
            self.__name = name
            self.__standard_attributes = standard_attributes
            self.__thumbnail_images = thumbnail_images
            self.__thumbnail_url = thumbnail_url
            self.__title = title

        def build(self):
            return SiteObject(absolute_href=self.__absolute_href, file_name=self.__file_name, full_size_images=self.__full_size_images, has_full_size_images=self.__has_full_size_images, has_thumbnail_images=self.__has_thumbnail_images, impl_attributes=self.__impl_attributes, name=self.__name, standard_attributes=self.__standard_attributes, thumbnail_images=self.__thumbnail_images, thumbnail_url=self.__thumbnail_url, title=self.__title)

        @property
        def absolute_href(self):
            '''
            :rtype: str
            '''

            return self.__absolute_href

        @property
        def file_name(self):
            '''
            :rtype: str
            '''

            return self.__file_name

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.site.site_object.SiteObject
            :rtype: pastpy.gen.site.site_object.SiteObject
            '''

            builder = cls()
            builder.absolute_href = template.absolute_href
            builder.file_name = template.file_name
            builder.full_size_images = template.full_size_images
            builder.has_full_size_images = template.has_full_size_images
            builder.has_thumbnail_images = template.has_thumbnail_images
            builder.impl_attributes = template.impl_attributes
            builder.name = template.name
            builder.standard_attributes = template.standard_attributes
            builder.thumbnail_images = template.thumbnail_images
            builder.thumbnail_url = template.thumbnail_url
            builder.title = template.title
            return builder

        @property
        def full_size_images(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            return self.__full_size_images

        @property
        def has_full_size_images(self):
            '''
            :rtype: bool
            '''

            return self.__has_full_size_images

        @property
        def has_thumbnail_images(self):
            '''
            :rtype: bool
            '''

            return self.__has_thumbnail_images

        @property
        def impl_attributes(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            return self.__impl_attributes

        @property
        def name(self):
            '''
            :rtype: str
            '''

            return self.__name

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

        def set_file_name(self, file_name):
            '''
            :type file_name: str
            '''

            if file_name is None:
                raise ValueError('file_name is required')
            if not isinstance(file_name, str):
                raise TypeError("expected file_name to be a str but it is a %s" % builtins.type(file_name))
            self.__file_name = file_name
            return self

        def set_full_size_images(self, full_size_images):
            '''
            :type full_size_images: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            if full_size_images is None:
                raise ValueError('full_size_images is required')
            if not (isinstance(full_size_images, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_image.SiteImage), full_size_images))) == 0):
                raise TypeError("expected full_size_images to be a tuple(pastpy.gen.site.site_image.SiteImage) but it is a %s" % builtins.type(full_size_images))
            self.__full_size_images = full_size_images
            return self

        def set_has_full_size_images(self, has_full_size_images):
            '''
            :type has_full_size_images: bool
            '''

            if has_full_size_images is None:
                raise ValueError('has_full_size_images is required')
            if not isinstance(has_full_size_images, bool):
                raise TypeError("expected has_full_size_images to be a bool but it is a %s" % builtins.type(has_full_size_images))
            self.__has_full_size_images = has_full_size_images
            return self

        def set_has_thumbnail_images(self, has_thumbnail_images):
            '''
            :type has_thumbnail_images: bool
            '''

            if has_thumbnail_images is None:
                raise ValueError('has_thumbnail_images is required')
            if not isinstance(has_thumbnail_images, bool):
                raise TypeError("expected has_thumbnail_images to be a bool but it is a %s" % builtins.type(has_thumbnail_images))
            self.__has_thumbnail_images = has_thumbnail_images
            return self

        def set_impl_attributes(self, impl_attributes):
            '''
            :type impl_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            if impl_attributes is None:
                raise ValueError('impl_attributes is required')
            if not (isinstance(impl_attributes, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_key_value_pair.SiteKeyValuePair), impl_attributes))) == 0):
                raise TypeError("expected impl_attributes to be a tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair) but it is a %s" % builtins.type(impl_attributes))
            self.__impl_attributes = impl_attributes
            return self

        def set_name(self, name):
            '''
            :type name: str
            '''

            if name is None:
                raise ValueError('name is required')
            if not isinstance(name, str):
                raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
            self.__name = name
            return self

        def set_standard_attributes(self, standard_attributes):
            '''
            :type standard_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            if standard_attributes is None:
                raise ValueError('standard_attributes is required')
            if not (isinstance(standard_attributes, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_key_value_pair.SiteKeyValuePair), standard_attributes))) == 0):
                raise TypeError("expected standard_attributes to be a tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair) but it is a %s" % builtins.type(standard_attributes))
            self.__standard_attributes = standard_attributes
            return self

        def set_thumbnail_images(self, thumbnail_images):
            '''
            :type thumbnail_images: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            if thumbnail_images is None:
                raise ValueError('thumbnail_images is required')
            if not (isinstance(thumbnail_images, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_image.SiteImage), thumbnail_images))) == 0):
                raise TypeError("expected thumbnail_images to be a tuple(pastpy.gen.site.site_image.SiteImage) but it is a %s" % builtins.type(thumbnail_images))
            self.__thumbnail_images = thumbnail_images
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
            self.__title = title
            return self

        @property
        def standard_attributes(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            return self.__standard_attributes

        @property
        def thumbnail_images(self):
            '''
            :rtype: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            return self.__thumbnail_images

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

        def update(self, site_object):
            '''
            :type absolute_href: str
            :type file_name: str
            :type full_size_images: tuple(pastpy.gen.site.site_image.SiteImage)
            :type has_full_size_images: bool
            :type has_thumbnail_images: bool
            :type impl_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            :type name: str
            :type standard_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            :type thumbnail_images: tuple(pastpy.gen.site.site_image.SiteImage)
            :type thumbnail_url: str
            :type title: str
            '''

            if isinstance(site_object, SiteObject):
                self.set_absolute_href(site_object.absolute_href)
                self.set_file_name(site_object.file_name)
                self.set_full_size_images(site_object.full_size_images)
                self.set_has_full_size_images(site_object.has_full_size_images)
                self.set_has_thumbnail_images(site_object.has_thumbnail_images)
                self.set_impl_attributes(site_object.impl_attributes)
                self.set_name(site_object.name)
                self.set_standard_attributes(site_object.standard_attributes)
                self.set_thumbnail_images(site_object.thumbnail_images)
                self.set_thumbnail_url(site_object.thumbnail_url)
                self.set_title(site_object.title)
            elif isinstance(site_object, dict):
                for key, value in site_object.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(site_object)
            return self

        @absolute_href.setter
        def absolute_href(self, absolute_href):
            '''
            :type absolute_href: str
            '''

            self.set_absolute_href(absolute_href)

        @file_name.setter
        def file_name(self, file_name):
            '''
            :type file_name: str
            '''

            self.set_file_name(file_name)

        @full_size_images.setter
        def full_size_images(self, full_size_images):
            '''
            :type full_size_images: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            self.set_full_size_images(full_size_images)

        @has_full_size_images.setter
        def has_full_size_images(self, has_full_size_images):
            '''
            :type has_full_size_images: bool
            '''

            self.set_has_full_size_images(has_full_size_images)

        @has_thumbnail_images.setter
        def has_thumbnail_images(self, has_thumbnail_images):
            '''
            :type has_thumbnail_images: bool
            '''

            self.set_has_thumbnail_images(has_thumbnail_images)

        @impl_attributes.setter
        def impl_attributes(self, impl_attributes):
            '''
            :type impl_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            self.set_impl_attributes(impl_attributes)

        @name.setter
        def name(self, name):
            '''
            :type name: str
            '''

            self.set_name(name)

        @standard_attributes.setter
        def standard_attributes(self, standard_attributes):
            '''
            :type standard_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
            '''

            self.set_standard_attributes(standard_attributes)

        @thumbnail_images.setter
        def thumbnail_images(self, thumbnail_images):
            '''
            :type thumbnail_images: tuple(pastpy.gen.site.site_image.SiteImage)
            '''

            self.set_thumbnail_images(thumbnail_images)

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
        ABSOLUTE_HREF = None
        FILE_NAME = None
        FULL_SIZE_IMAGES = None
        HAS_FULL_SIZE_IMAGES = None
        HAS_THUMBNAIL_IMAGES = None
        IMPL_ATTRIBUTES = None
        NAME = None
        STANDARD_ATTRIBUTES = None
        THUMBNAIL_IMAGES = None
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
            return (cls.ABSOLUTE_HREF, cls.FILE_NAME, cls.FULL_SIZE_IMAGES, cls.HAS_FULL_SIZE_IMAGES, cls.HAS_THUMBNAIL_IMAGES, cls.IMPL_ATTRIBUTES, cls.NAME, cls.STANDARD_ATTRIBUTES, cls.THUMBNAIL_IMAGES, cls.THUMBNAIL_URL, cls.TITLE,)

    FieldMetadata.ABSOLUTE_HREF = FieldMetadata('absolute_href', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.FILE_NAME = FieldMetadata('file_name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.FULL_SIZE_IMAGES = FieldMetadata('full_size_images', tuple, None)
    FieldMetadata.HAS_FULL_SIZE_IMAGES = FieldMetadata('has_full_size_images', bool, None)
    FieldMetadata.HAS_THUMBNAIL_IMAGES = FieldMetadata('has_thumbnail_images', bool, None)
    FieldMetadata.IMPL_ATTRIBUTES = FieldMetadata('impl_attributes', tuple, None)
    FieldMetadata.NAME = FieldMetadata('name', pastpy.gen.non_blank_string.NonBlankString, None)
    FieldMetadata.STANDARD_ATTRIBUTES = FieldMetadata('standard_attributes', tuple, None)
    FieldMetadata.THUMBNAIL_IMAGES = FieldMetadata('thumbnail_images', tuple, None)
    FieldMetadata.THUMBNAIL_URL = FieldMetadata('thumbnail_url', str, None)
    FieldMetadata.TITLE = FieldMetadata('title', pastpy.gen.non_blank_string.NonBlankString, None)

    def __init__(
        self,
        absolute_href,
        file_name,
        full_size_images,
        has_full_size_images,
        has_thumbnail_images,
        impl_attributes,
        name,
        standard_attributes,
        thumbnail_images,
        thumbnail_url,
        title,
    ):
        '''
        :type absolute_href: str
        :type file_name: str
        :type full_size_images: tuple(pastpy.gen.site.site_image.SiteImage)
        :type has_full_size_images: bool
        :type has_thumbnail_images: bool
        :type impl_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
        :type name: str
        :type standard_attributes: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
        :type thumbnail_images: tuple(pastpy.gen.site.site_image.SiteImage)
        :type thumbnail_url: str
        :type title: str
        '''

        if absolute_href is None:
            raise ValueError('absolute_href is required')
        if not isinstance(absolute_href, str):
            raise TypeError("expected absolute_href to be a str but it is a %s" % builtins.type(absolute_href))
        self.__absolute_href = absolute_href

        if file_name is None:
            raise ValueError('file_name is required')
        if not isinstance(file_name, str):
            raise TypeError("expected file_name to be a str but it is a %s" % builtins.type(file_name))
        self.__file_name = file_name

        if full_size_images is None:
            raise ValueError('full_size_images is required')
        if not (isinstance(full_size_images, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_image.SiteImage), full_size_images))) == 0):
            raise TypeError("expected full_size_images to be a tuple(pastpy.gen.site.site_image.SiteImage) but it is a %s" % builtins.type(full_size_images))
        self.__full_size_images = full_size_images

        if has_full_size_images is None:
            raise ValueError('has_full_size_images is required')
        if not isinstance(has_full_size_images, bool):
            raise TypeError("expected has_full_size_images to be a bool but it is a %s" % builtins.type(has_full_size_images))
        self.__has_full_size_images = has_full_size_images

        if has_thumbnail_images is None:
            raise ValueError('has_thumbnail_images is required')
        if not isinstance(has_thumbnail_images, bool):
            raise TypeError("expected has_thumbnail_images to be a bool but it is a %s" % builtins.type(has_thumbnail_images))
        self.__has_thumbnail_images = has_thumbnail_images

        if impl_attributes is None:
            raise ValueError('impl_attributes is required')
        if not (isinstance(impl_attributes, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_key_value_pair.SiteKeyValuePair), impl_attributes))) == 0):
            raise TypeError("expected impl_attributes to be a tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair) but it is a %s" % builtins.type(impl_attributes))
        self.__impl_attributes = impl_attributes

        if name is None:
            raise ValueError('name is required')
        if not isinstance(name, str):
            raise TypeError("expected name to be a str but it is a %s" % builtins.type(name))
        self.__name = name

        if standard_attributes is None:
            raise ValueError('standard_attributes is required')
        if not (isinstance(standard_attributes, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_key_value_pair.SiteKeyValuePair), standard_attributes))) == 0):
            raise TypeError("expected standard_attributes to be a tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair) but it is a %s" % builtins.type(standard_attributes))
        self.__standard_attributes = standard_attributes

        if thumbnail_images is None:
            raise ValueError('thumbnail_images is required')
        if not (isinstance(thumbnail_images, tuple) and len(list(filterfalse(lambda _: isinstance(_, pastpy.gen.site.site_image.SiteImage), thumbnail_images))) == 0):
            raise TypeError("expected thumbnail_images to be a tuple(pastpy.gen.site.site_image.SiteImage) but it is a %s" % builtins.type(thumbnail_images))
        self.__thumbnail_images = thumbnail_images

        if thumbnail_url is None:
            raise ValueError('thumbnail_url is required')
        if not isinstance(thumbnail_url, str):
            raise TypeError("expected thumbnail_url to be a str but it is a %s" % builtins.type(thumbnail_url))
        self.__thumbnail_url = thumbnail_url

        if title is None:
            raise ValueError('title is required')
        if not isinstance(title, str):
            raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
        self.__title = title

    def __eq__(self, other):
        if self.absolute_href != other.absolute_href:
            return False
        if self.file_name != other.file_name:
            return False
        if self.full_size_images != other.full_size_images:
            return False
        if self.has_full_size_images != other.has_full_size_images:
            return False
        if self.has_thumbnail_images != other.has_thumbnail_images:
            return False
        if self.impl_attributes != other.impl_attributes:
            return False
        if self.name != other.name:
            return False
        if self.standard_attributes != other.standard_attributes:
            return False
        if self.thumbnail_images != other.thumbnail_images:
            return False
        if self.thumbnail_url != other.thumbnail_url:
            return False
        if self.title != other.title:
            return False
        return True

    def __hash__(self):
        return hash((self.absolute_href, self.file_name, self.full_size_images, self.has_full_size_images, self.has_thumbnail_images, self.impl_attributes, self.name, self.standard_attributes, self.thumbnail_images, self.thumbnail_url, self.title,))

    def __iter__(self):
        return iter((self.absolute_href, self.file_name, self.full_size_images, self.has_full_size_images, self.has_thumbnail_images, self.impl_attributes, self.name, self.standard_attributes, self.thumbnail_images, self.thumbnail_url, self.title,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('file_name=' + "'" + self.file_name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('full_size_images=' + repr(self.full_size_images))
        field_reprs.append('has_full_size_images=' + repr(self.has_full_size_images))
        field_reprs.append('has_thumbnail_images=' + repr(self.has_thumbnail_images))
        field_reprs.append('impl_attributes=' + repr(self.impl_attributes))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('standard_attributes=' + repr(self.standard_attributes))
        field_reprs.append('thumbnail_images=' + repr(self.thumbnail_images))
        field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteObject(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('absolute_href=' + "'" + self.absolute_href.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('file_name=' + "'" + self.file_name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('full_size_images=' + repr(self.full_size_images))
        field_reprs.append('has_full_size_images=' + repr(self.has_full_size_images))
        field_reprs.append('has_thumbnail_images=' + repr(self.has_thumbnail_images))
        field_reprs.append('impl_attributes=' + repr(self.impl_attributes))
        field_reprs.append('name=' + "'" + self.name.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('standard_attributes=' + repr(self.standard_attributes))
        field_reprs.append('thumbnail_images=' + repr(self.thumbnail_images))
        field_reprs.append('thumbnail_url=' + "'" + self.thumbnail_url.encode('ascii', 'replace').decode('ascii') + "'")
        field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        return 'SiteObject(' + ', '.join(field_reprs) + ')'

    @property
    def absolute_href(self):
        '''
        :rtype: str
        '''

        return self.__absolute_href

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def file_name(self):
        '''
        :rtype: str
        '''

        return self.__file_name

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        absolute_href = _dict.get("absolute_href")
        if absolute_href is None:
            raise KeyError("absolute_href")
        __builder.absolute_href = absolute_href

        file_name = _dict.get("file_name")
        if file_name is None:
            raise KeyError("file_name")
        __builder.file_name = file_name

        full_size_images = _dict.get("full_size_images")
        if full_size_images is None:
            raise KeyError("full_size_images")
        full_size_images = tuple(pastpy.gen.site.site_image.SiteImage.from_builtins(element0) for element0 in full_size_images)
        __builder.full_size_images = full_size_images

        has_full_size_images = _dict.get("has_full_size_images")
        if has_full_size_images is None:
            raise KeyError("has_full_size_images")
        __builder.has_full_size_images = has_full_size_images

        has_thumbnail_images = _dict.get("has_thumbnail_images")
        if has_thumbnail_images is None:
            raise KeyError("has_thumbnail_images")
        __builder.has_thumbnail_images = has_thumbnail_images

        impl_attributes = _dict.get("impl_attributes")
        if impl_attributes is None:
            raise KeyError("impl_attributes")
        impl_attributes = tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair.from_builtins(element0) for element0 in impl_attributes)
        __builder.impl_attributes = impl_attributes

        name = _dict.get("name")
        if name is None:
            raise KeyError("name")
        __builder.name = name

        standard_attributes = _dict.get("standard_attributes")
        if standard_attributes is None:
            raise KeyError("standard_attributes")
        standard_attributes = tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair.from_builtins(element0) for element0 in standard_attributes)
        __builder.standard_attributes = standard_attributes

        thumbnail_images = _dict.get("thumbnail_images")
        if thumbnail_images is None:
            raise KeyError("thumbnail_images")
        thumbnail_images = tuple(pastpy.gen.site.site_image.SiteImage.from_builtins(element0) for element0 in thumbnail_images)
        __builder.thumbnail_images = thumbnail_images

        thumbnail_url = _dict.get("thumbnail_url")
        if thumbnail_url is None:
            raise KeyError("thumbnail_url")
        __builder.thumbnail_url = thumbnail_url

        title = _dict.get("title")
        if title is None:
            raise KeyError("title")
        __builder.title = title

        return __builder.build()

    @property
    def full_size_images(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_image.SiteImage)
        '''

        return self.__full_size_images

    @property
    def has_full_size_images(self):
        '''
        :rtype: bool
        '''

        return self.__has_full_size_images

    @property
    def has_thumbnail_images(self):
        '''
        :rtype: bool
        '''

        return self.__has_thumbnail_images

    @property
    def impl_attributes(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
        '''

        return self.__impl_attributes

    @property
    def name(self):
        '''
        :rtype: str
        '''

        return self.__name

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.site.site_object.SiteObject
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'absolute_href':
                init_kwds['absolute_href'] = iprot.read_string()
            elif ifield_name == 'file_name':
                init_kwds['file_name'] = iprot.read_string()
            elif ifield_name == 'full_size_images':
                init_kwds['full_size_images'] = tuple([pastpy.gen.site.site_image.SiteImage.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'has_full_size_images':
                init_kwds['has_full_size_images'] = iprot.read_bool()
            elif ifield_name == 'has_thumbnail_images':
                init_kwds['has_thumbnail_images'] = iprot.read_bool()
            elif ifield_name == 'impl_attributes':
                init_kwds['impl_attributes'] = tuple([pastpy.gen.site.site_key_value_pair.SiteKeyValuePair.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'name':
                init_kwds['name'] = iprot.read_string()
            elif ifield_name == 'standard_attributes':
                init_kwds['standard_attributes'] = tuple([pastpy.gen.site.site_key_value_pair.SiteKeyValuePair.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'thumbnail_images':
                init_kwds['thumbnail_images'] = tuple([pastpy.gen.site.site_image.SiteImage.read(iprot) for _ in xrange(iprot.read_list_begin()[1])] + (iprot.read_list_end() is None and []))
            elif ifield_name == 'thumbnail_url':
                init_kwds['thumbnail_url'] = iprot.read_string()
            elif ifield_name == 'title':
                init_kwds['title'] = iprot.read_string()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    @property
    def standard_attributes(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_key_value_pair.SiteKeyValuePair)
        '''

        return self.__standard_attributes

    @property
    def thumbnail_images(self):
        '''
        :rtype: tuple(pastpy.gen.site.site_image.SiteImage)
        '''

        return self.__thumbnail_images

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
        dict_["absolute_href"] = self.absolute_href
        dict_["file_name"] = self.file_name
        dict_["full_size_images"] = tuple(element0.to_builtins() for element0 in self.full_size_images)
        dict_["has_full_size_images"] = self.has_full_size_images
        dict_["has_thumbnail_images"] = self.has_thumbnail_images
        dict_["impl_attributes"] = tuple(element0.to_builtins() for element0 in self.impl_attributes)
        dict_["name"] = self.name
        dict_["standard_attributes"] = tuple(element0.to_builtins() for element0 in self.standard_attributes)
        dict_["thumbnail_images"] = tuple(element0.to_builtins() for element0 in self.thumbnail_images)
        dict_["thumbnail_url"] = self.thumbnail_url
        dict_["title"] = self.title
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.site.site_object.SiteObject
        '''

        oprot.write_struct_begin('SiteObject')

        oprot.write_field_begin(name='absolute_href', type=11, id=None)
        oprot.write_string(self.absolute_href)
        oprot.write_field_end()

        oprot.write_field_begin(name='file_name', type=11, id=None)
        oprot.write_string(self.file_name)
        oprot.write_field_end()

        oprot.write_field_begin(name='full_size_images', type=15, id=None)
        oprot.write_list_begin(12, len(self.full_size_images))
        for _0 in self.full_size_images:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='has_full_size_images', type=2, id=None)
        oprot.write_bool(self.has_full_size_images)
        oprot.write_field_end()

        oprot.write_field_begin(name='has_thumbnail_images', type=2, id=None)
        oprot.write_bool(self.has_thumbnail_images)
        oprot.write_field_end()

        oprot.write_field_begin(name='impl_attributes', type=15, id=None)
        oprot.write_list_begin(12, len(self.impl_attributes))
        for _0 in self.impl_attributes:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='name', type=11, id=None)
        oprot.write_string(self.name)
        oprot.write_field_end()

        oprot.write_field_begin(name='standard_attributes', type=15, id=None)
        oprot.write_list_begin(12, len(self.standard_attributes))
        for _0 in self.standard_attributes:
            _0.write(oprot)
        oprot.write_list_end()
        oprot.write_field_end()

        oprot.write_field_begin(name='thumbnail_images', type=15, id=None)
        oprot.write_list_begin(12, len(self.thumbnail_images))
        for _0 in self.thumbnail_images:
            _0.write(oprot)
        oprot.write_list_end()
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
