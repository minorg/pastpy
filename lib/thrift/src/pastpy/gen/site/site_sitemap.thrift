namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_objects_list.thrift"

struct SiteSitemap {
    non_blank_string.NonBlankString lastmod;
    list<site_object.SiteObject> objects;
    list<site_objects_list.SiteObjectsList> objects_list_pages;
}
