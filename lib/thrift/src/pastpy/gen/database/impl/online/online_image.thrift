namespace * pastpy.gen.database.impl.online

include "online_image_type.thrift"
include "thryft/native/url.thrift"

struct OnlineImage {
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

    online_image_type.OnlineImageType type;
}
