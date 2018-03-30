namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"

struct SiteConfiguration {
    non_blank_string.NonBlankString copyright_holder = "Your Collection";
    non_blank_string.NonBlankString google_custom_search_engine_id;
    non_blank_string.NonBlankString name = "Your Collection";
    non_blank_string.NonBlankString output_dir_path = "site";
    optional non_blank_string.NonBlankString institution_name;
    optional non_blank_string.NonBlankString template_dir_path;
}
