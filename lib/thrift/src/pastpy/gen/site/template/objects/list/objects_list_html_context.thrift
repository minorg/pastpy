namespace * pastpy.gen.site.template.objects.list

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_pagination.thrift"

struct ObjectsListHtmlContext {
    non_blank_string.NonBlankString absolute_href;
    site_metadata.SiteMetadata metadata;
    list<site_object.SiteObject> objects;
    site_pagination.SitePagination pagination;
}
