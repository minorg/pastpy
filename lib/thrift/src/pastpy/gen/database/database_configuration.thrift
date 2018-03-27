namespace * pastpy.gen.database

include "pastpy/gen/database/impl/dbf/dbf_database_configuration.thrift"
include "pastpy/gen/database/impl/online/online_database_configuration.thrift"

struct DatabaseConfiguration {
    optional dbf_database_configuration.DbfDatabaseConfiguration dbf;
    optional online_database_configuration.OnlineDatabaseConfiguration online;
}
