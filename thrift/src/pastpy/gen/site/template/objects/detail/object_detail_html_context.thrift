namespace * pastpy.gen.site.template.objects.detail

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_configuration.thrift"
include "pastpy/gen/site/site_object.thrift"
include "pastpy/gen/site/template/footer_html_context.thrift"
include "pastpy/gen/site/template/navbar_html_context.thrift"

struct ObjectDetailHtmlContext {
    site_configuration.SiteConfiguration configuration;
    footer_html_context.FooterHtmlContext footer;
    navbar_html_context.NavbarHtmlContext navbar;
    site_object.SiteObject object;
    non_blank_string.NonBlankString root_relative_href;
}