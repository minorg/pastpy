namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_configuration.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_pagination_page_number.thrift"

struct SiteSitemap {
    site_configuration.SiteConfiguration configuration;
    non_blank_string.NonBlankString lastmod;
    list<site_object.SiteObject> objects;
    list<site_pagination_page_number.SitePaginationPageNumber> objects_list_page_numbers;
}
