namespace * pastpy.gen.site

include "pastpy/gen/site/site_pagination_page_number.thrift"

struct SitePagination {
    site_pagination_page_number.SitePaginationPageNumber current_page_number;
    site_pagination_page_number.SitePaginationPageNumber next_page_number;
    site_pagination_page_number.SitePaginationPageNumber previous_page_number;
    list<site_pagination_page_number.SitePaginationPageNumber> visible_page_numbers;
}
