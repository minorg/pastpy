namespace * pastpy.impl.online

include "thryft/native/url.thrift"

struct ObjectsListItem {
    // @validation {"blank": false, "minLength": 1}
    string detail_href;
    // @validation {"blank": false, "minLength": 1}
    string record_type;
    url.Url thumbnail_src;
    // @validation {"blank": false, "minLength": 1}
    string title;
}
