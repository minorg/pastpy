namespace * pastpy.gen.online

include "online_image.thrift"

struct OnlineObjectDetail {
    // @validation {"blank": false, "minLength": 1}
    string guid;
    // @validation {"blank": false, "minLength": 1}
    string id;
    optional map<string, string> attributes;
    optional list<online_image.OnlineImage> related_photos;
}
