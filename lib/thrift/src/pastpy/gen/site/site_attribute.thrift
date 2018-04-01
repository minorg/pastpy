namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/variant.thrift"

struct SiteAttribute {
    non_blank_string.NonBlankString name;
    variant.Variant value;
}
