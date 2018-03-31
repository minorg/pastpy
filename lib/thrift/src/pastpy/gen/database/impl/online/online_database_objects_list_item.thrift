namespace * pastpy.gen.database.impl.online

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/url.thrift"

struct OnlineDatabaseObjectsListItem {
    non_blank_string.NonBlankString detail_href;
    non_blank_string.NonBlankString record_type;
    non_blank_string.NonBlankString title;
    optional url.Url thumbnail_url;
}
