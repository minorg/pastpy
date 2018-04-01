namespace * pastpy.gen.site

include "pastpy/gen/true_bool.thrift"

// @union
struct SiteNavItems {
    optional true_bool.TrueBool home;
    optional true_bool.TrueBool objects;
}