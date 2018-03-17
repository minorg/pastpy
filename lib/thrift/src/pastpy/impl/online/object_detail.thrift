namespace * pastpy.impl.online

include "image.thrift"

struct ObjectDetail {
    optional list<image.Image> related_photos;
}
