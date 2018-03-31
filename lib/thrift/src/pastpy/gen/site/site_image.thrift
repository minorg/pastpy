namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/url.thrift"

struct SiteImage {
    url.Url full_size_url;
    url.Url thumbnail_url;
    non_blank_string.NonBlankString title;
}
