namespace * pastpy.gen.database.impl.dbf

include "pastpy/gen/non_blank_string.thrift"

struct DbfDatabaseConfiguration {
    // Path to PastPerfect images directory. Defaults to install\Images.
    optional non_blank_string.NonBlankString pp_images_dir_path;

    // Path to PastPerfect installation directory e.g., c:\pp5
    optional non_blank_string.NonBlankString pp_install_dir_path;

    // Path to PastPerfect OBJECTS.DBF file. Defaults to install\Data\OBJECTS.DBF.
    optional non_blank_string.NonBlankString pp_objects_dbf_file_path;
}
