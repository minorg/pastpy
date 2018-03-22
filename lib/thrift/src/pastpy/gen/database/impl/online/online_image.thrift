namespace * pastpy.gen.database.impl.online

include "pastpy/gen/database/impl/online/online_image_type.thrift"
include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/url.thrift"

struct OnlineImage {
    url.Url full_size_url;

    non_blank_string.NonBlankString mediaid;

    non_blank_string.NonBlankString objectid;

    non_blank_string.NonBlankString src;

    url.Url thumbnail_url;

    non_blank_string.NonBlankString title;

    online_image_type.OnlineImageType type;
}
