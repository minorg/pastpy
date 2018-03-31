namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_nav_items.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_objects_list_page_number.thrift"

struct SiteObjectsListPage {
    non_blank_string.NonBlankString absolute_href;
    site_nav_items.SiteNavItems nav_items;
    site_objects_list_page_number.SiteObjectsListPageNumber next_page_number;
    list<site_object.SiteObject> objects;
    list<site_objects_list_page_number.SiteObjectsListPageNumber> page_numbers;
    site_objects_list_page_number.SiteObjectsListPageNumber previous_page_number;
}
