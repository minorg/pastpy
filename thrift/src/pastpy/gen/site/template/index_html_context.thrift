namespace * pastpy.gen.site.template

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_configuration.thrift"
include "pastpy/gen/site/template/footer_html_context.thrift"
include "pastpy/gen/site/template/navbar_html_context.thrift"

struct IndexHtmlContext {
    site_configuration.SiteConfiguration configuration;
    footer_html_context.FooterHtmlContext footer;
    bool has_featured_searches;
    navbar_html_context.NavbarHtmlContext navbar;
    non_blank_string.NonBlankString root_relative_href;
}
