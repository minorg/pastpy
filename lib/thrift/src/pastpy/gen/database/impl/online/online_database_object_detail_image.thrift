namespace * pastpy.gen.database.impl.online

include "pastpy/gen/database/impl/online/online_database_object_detail_image_type.thrift"
include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/url.thrift"

struct OnlineDatabaseObjectDetailImage {
    url.Url full_size_url;

    non_blank_string.NonBlankString mediaid;

    non_blank_string.NonBlankString objectid;

    non_blank_string.NonBlankString src;

    url.Url thumbnail_url;

    non_blank_string.NonBlankString title;

    online_database_object_detail_image_type.OnlineDatabaseObjectDetailImageType type;
}
