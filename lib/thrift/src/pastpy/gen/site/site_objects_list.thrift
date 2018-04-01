namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_objects_list_page_number.thrift"

struct SiteObjectsList {
    non_blank_string.NonBlankString absolute_href;
    site_metadata.SiteMetadata metadata;
    site_objects_list_page_number.SiteObjectsListPageNumber next_page_number;
    list<site_object.SiteObject> objects;
    site_objects_list_page_number.SiteObjectsListPageNumber previous_page_number;
    list<site_objects_list_page_number.SiteObjectsListPageNumber> visible_page_numbers;
}
