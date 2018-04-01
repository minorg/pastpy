namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"

struct SiteFeaturedSearch {
    non_blank_string.NonBlankString name;
    non_blank_string.NonBlankString query;
}
