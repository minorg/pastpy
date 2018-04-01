namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"
include "pastpy/gen/site/site_featured_search.thrift"
include "thryft/native/url.thrift"

struct SiteConfiguration {
    url.Url base_url;
    non_blank_string.NonBlankString copyright_holder = "Your Collection";
    non_blank_string.NonBlankString google_custom_search_engine_id;
    non_blank_string.NonBlankString name = "Your Collection";
    non_blank_string.NonBlankString output_dir_path = "site";
    optional list<site_featured_search.SiteFeaturedSearch> featured_searches;
    optional non_blank_string.NonBlankString institution_name;
    optional non_blank_string.NonBlankString template_dir_path;
    optional non_blank_string.NonBlankString theme_css_file_path;
}
