namespace * pastpy.gen.site

include "pastpy/gen/non_blank_string.thrift"

struct SiteConfiguration {
    non_blank_string.NonBlankString copyright_holder;
    non_blank_string.NonBlankString database;
    non_blank_string.NonBlankString name;
    non_blank_string.NonBlankString output_dir_path;
    optional non_blank_string.NonBlankString templates_dir_path;
}
