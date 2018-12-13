namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "thryft/native/url.thrift"

struct SiteImage {
    optional url.Url full_size_url;
    optional url.Url thumbnail_url;
    optional non_blank_string.NonBlankString title;
}
