namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_pagination.thrift"

struct SiteObjectsList {
    non_blank_string.NonBlankString absolute_href;
    site_metadata.SiteMetadata metadata;
    list<site_object.SiteObject> objects;
    site_pagination.SitePagination pagination;
}
