namespace * pastpy.gen.site

include "pastpy/gen/name_value_pair.thrift"
include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_image.thrift"
include "thryft/native/url.thrift"

struct SiteObject {
    non_blank_string.NonBlankString absolute_href;
    non_blank_string.NonBlankString file_name;
    list<site_image.SiteImage> full_size_images;
    bool has_full_size_images;
    bool has_thumbnail_images;
    non_blank_string.NonBlankString id;
    list<name_value_pair.NameValuePair> impl_attributes_list;
    non_blank_string.NonBlankString name;
    list<name_value_pair.NameValuePair> standard_attributes_list;
    list<name_value_pair.NameValuePair> standard_attributes_list_xml;
    map<non_blank_string.NonBlankString, non_blank_string.NonBlankString> standard_attributes_map;
    map<non_blank_string.NonBlankString, non_blank_string.NonBlankString> standard_attributes_map_json;
    list<site_image.SiteImage> thumbnail_images;
    url.Url thumbnail_url;
    non_blank_string.NonBlankString title;
    optional non_blank_string.NonBlankString date;
    optional non_blank_string.NonBlankString description;
}
