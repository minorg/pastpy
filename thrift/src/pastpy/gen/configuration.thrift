namespace * pastpy.gen

include "pastpy/gen/database/database_configuration.thrift"
include "pastpy/gen/site/site_configuration.thrift"

struct Configuration {
    database_configuration.DatabaseConfiguration database;
    optional site_configuration.SiteConfiguration site;
}
