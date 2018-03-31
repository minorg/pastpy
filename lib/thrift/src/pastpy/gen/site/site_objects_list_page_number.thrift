namespace * pastpy.gen.site

struct SiteObjectsListPageNumber {
    bool active;
    bool enabled;
    // @validation {"min": 1}
    i32 number;
}
