namespace * pastpy.impl.online

include "image.thrift"

struct ObjectDetail {
    optional map<string, string> attributes;
    optional list<image.Image> related_photos;
}
