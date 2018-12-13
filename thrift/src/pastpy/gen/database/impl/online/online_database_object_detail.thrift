namespace * pastpy.gen.database.impl.online

include "pastpy/gen/database/impl/online/online_database_object_detail_image.thrift"
include "pastpy/gen/non_blank_string.thrift"

struct OnlineDatabaseObjectDetail {
    map<non_blank_string.NonBlankString, non_blank_string.NonBlankString> attributes;
    non_blank_string.NonBlankString guid;
    non_blank_string.NonBlankString id;
    list<online_database_object_detail_image.OnlineDatabaseObjectDetailImage> related_photos;
}
