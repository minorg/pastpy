namespace * pastpy.gen.online

include "online_image.thrift"

struct OnlineObjectDetail {
    map<string, string> attributes;
    // @validation {"blank": false, "minLength": 1}
    string guid;
    // @validation {"blank": false, "minLength": 1}
    string id;
    list<online_image.OnlineImage> related_photos;
}
