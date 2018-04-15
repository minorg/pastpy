namespace * pastpy.gen.site.template.objects.list

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/site_pagination.thrift"
include "pastpy/gen/site/template/footer_html_context.thrift"
include "pastpy/gen/site/template/navbar_html_context.thrift"

struct ObjectsListHtmlContext {
    non_blank_string.NonBlankString absolute_href;
    footer_html_context.FooterHtmlContext footer;
    navbar_html_context.NavbarHtmlContext navbar;
    list<site_object.SiteObject> objects;
    site_pagination.SitePagination pagination;
    non_blank_string.NonBlankString root_relative_href;
}
