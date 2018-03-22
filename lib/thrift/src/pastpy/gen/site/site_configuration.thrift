namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"

struct SiteConfiguration {
    non_blank_string.NonBlankString copyright_holder = "Your Collection";
    non_blank_string.NonBlankString database = "c:\\pp5";
    non_blank_string.NonBlankString name = "Your Collection";
    non_blank_string.NonBlankString output_dir_path = "site";
    optional non_blank_string.NonBlankString templates_dir_path;
}
