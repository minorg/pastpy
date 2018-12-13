namespace * pastpy.gen.database.impl.online

include "pastpy/gen/non_blank_string.thrift"

struct OnlineDatabaseConfiguration {
    // Collection name of PastPerfect Online site e.g., yourcollection in http://yourcollection.pastperfectonline.com
    non_blank_string.NonBlankString collection_name;

    // Path for downloaded files, defaults to collection name
    optional non_blank_string.NonBlankString download_dir_path;
}
