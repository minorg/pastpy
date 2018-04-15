namespace * pastpy.gen.site.template.objects.detail

include "pastpy/gen/site/site_metadata.thrift"
include "pastpy/gen/site/site_object.thrift"

struct ObjectDetailHtmlContext {
    site_metadata.SiteMetadata metadata;
    site_object.SiteObject object;
}
