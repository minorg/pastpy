namespace * pastpy.impl.online

include "image_type.thrift"
include "thryft/native/url.thrift"

struct Image {
    url.Url full_size_url;

    // @validation {"blank": false, "minLength": 1}
    string mediaid;

    // @validation {"blank": false, "minLength": 1}
    string objectid;

    // @validation {"blank": false, "minLength": 1}
    string src;

    url.Url thumbnail_url;

    // @validation {"blank": false, "minLength": 1}
    string title;

    image_type.ImageType type;
}
