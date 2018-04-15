namespace * pastpy.gen

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/variant.thrift"

struct NameValuePair {
    non_blank_string.NonBlankString name;
    variant.Variant value;
}
