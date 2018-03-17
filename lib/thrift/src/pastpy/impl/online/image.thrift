namespace * pastpy.impl.online

include "thryft/native/url.thrift"

struct Image {
    url.Url full_size_url;

    url.Url thumbnail_url;

    // @validation {"blank": false, "minLength": 1}
    string title;
}
