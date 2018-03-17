namespace * pastpy.impl.online

include "image.thrift"

struct ObjectDetail {
    // @validation {"blank": false, "minLength": 1}
    string guid;
    // @validation {"blank": false, "minLength": 1}
    string id;
    optional map<string, string> attributes;
    optional list<image.Image> related_photos;
}
