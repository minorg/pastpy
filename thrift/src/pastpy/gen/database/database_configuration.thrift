namespace * pastpy.gen.database

include "pastpy/gen/database/impl/dbf/dbf_database_configuration.thrift"
include "pastpy/gen/database/impl/dummy/dummy_database_configuration.thrift"
include "pastpy/gen/database/impl/online/online_database_configuration.thrift"

// @union
struct DatabaseConfiguration {
    optional dbf_database_configuration.DbfDatabaseConfiguration dbf;
    optional dummy_database_configuration.DummyDatabaseConfiguration dummy;
    optional online_database_configuration.OnlineDatabaseConfiguration online;
}
