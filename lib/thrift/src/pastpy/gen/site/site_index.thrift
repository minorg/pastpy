namespace * pastpy.gen.site

include "pastpy/gen/site/site_metadata.thrift"

struct SiteIndex {
    bool has_featured_searches;
    site_metadata.SiteMetadata metadata;
}
