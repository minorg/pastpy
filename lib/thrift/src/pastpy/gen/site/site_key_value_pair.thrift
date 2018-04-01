namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/variant.thrift"

struct SiteKeyValuePair {
    non_blank_string.NonBlankString key;
    variant.Variant value;
}
