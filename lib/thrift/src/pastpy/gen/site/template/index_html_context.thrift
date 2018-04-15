namespace * pastpy.gen.site.template

include "pastpy/gen/site/site_metadata.thrift"

struct IndexHtmlContext {
    bool has_featured_searches;
    site_metadata.SiteMetadata metadata;
}
