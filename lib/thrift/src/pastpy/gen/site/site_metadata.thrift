namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_configuration.thrift"
include "pastpy/gen/site/site_nav_items.thrift"

struct SiteMetadata {
    site_configuration.SiteConfiguration configuration;
    i32 current_year;
    site_nav_items.SiteNavItems nav_items;
    non_blank_string.NonBlankString root_relative_href;
}
