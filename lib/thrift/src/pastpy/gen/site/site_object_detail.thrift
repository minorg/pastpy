namespace * pastpy.gen.site

include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_object.thrift"

struct SiteObjectDetail {
    site_metadata.SiteMetadata metadata;
    site_object.SiteObject object;
}
