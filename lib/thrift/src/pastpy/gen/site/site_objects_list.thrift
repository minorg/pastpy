namespace * pastpy.gen.site

include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_objects_list_page.thrift"

struct SiteObjectsList {
    site_metadata.SiteMetadata metadata;
    list<site_objects_list_page.SiteObjectsListPage> pages;
}
