namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_image.thrift"
include "pastpy/gen/site/site_key_value_pair.thrift"
include "thryft/native/url.thrift"

struct SiteObject {
    non_blank_string.NonBlankString absolute_href;
    non_blank_string.NonBlankString file_name;
    list<site_image.SiteImage> full_size_images;
    bool has_full_size_images;
    bool has_thumbnail_images;
    list<site_key_value_pair.SiteKeyValuePair> impl_attributes;
    non_blank_string.NonBlankString name;
    non_blank_string.NonBlankString relative_href;
    list<site_key_value_pair.SiteKeyValuePair> standard_attributes;
    list<site_image.SiteImage> thumbnail_images;
    url.Url thumbnail_url;
    non_blank_string.NonBlankString title;
}
