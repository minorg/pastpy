namespace * pastpy.gen.database.impl.online

include "pastpy/gen/database/impl/online/online_image.thrift"
include "pastpy/gen/non_blank_string.thrift"

struct OnlineObjectDetail {
    map<non_blank_string.NonBlankString, non_blank_string.NonBlankString> attributes;
    non_blank_string.NonBlankString guid;
    non_blank_string.NonBlankString id;
    list<online_image.OnlineImage> related_photos;
}
