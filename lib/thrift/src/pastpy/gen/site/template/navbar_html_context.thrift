namespace * pastpy.gen.site.template

include "pastpy/gen/true_bool.thrift"

// @union
struct NavbarHtmlContext {
    optional true_bool.TrueBool home;
    optional true_bool.TrueBool objects;
}