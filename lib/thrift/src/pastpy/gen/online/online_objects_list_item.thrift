namespace * pastpy.gen.online

include "thryft/native/url.thrift"

struct OnlineObjectsListItem {
    // @validation {"blank": false, "minLength": 1}
    string detail_href;
    // @validation {"blank": false, "minLength": 1}
    string record_type;
    // @validation {"blank": false, "minLength": 1}
    string title;
    optional url.Url thumbnail_url;
}
