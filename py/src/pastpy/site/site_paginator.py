from pastpy.gen.site.site_pagination import SitePagination
from pastpy.gen.site.site_pagination_page_number import SitePaginationPageNumber
from pastpy.site.site_paginator_page import SitePaginatorPage


class SitePaginator(object):
    def paginate(self, *, objects, objects_per_page):
        objects = list(reversed(list(objects)))
        objects_chunks = []
        while objects:
            objects_chunk = []
            while objects and len(objects_chunk) < objects_per_page:
                objects_chunk.append(objects.pop())
            objects_chunks.append(objects_chunk)

        pages = []
        for page_i, objects_chunk in enumerate(objects_chunks):
            # *page_number* is one-based
            # current_page_number = page_i + 1

            pagination_builder = SitePagination.builder()

            pagination_builder.current_page_number = SitePaginationPageNumber(
                active=True,
                enabled=True,
                number=page_i + 1
            )

            pagination_builder.next_page_number = SitePaginationPageNumber(
                active=False,
                enabled=page_i + 1 < len(objects_chunks),
                number=page_i + 2
            )
            pagination_builder.previous_page_number = SitePaginationPageNumber(
                active=False,
                enabled=page_i > 0,
                number=page_i
            )

            visible_page_numbers = []
            objects_page_range = self.__page_range(
                page_i=page_i, page_min=0, page_max=len(objects_chunks) - 1, window=10)
            for objects_page_range_i in objects_page_range:
                visible_page_numbers.append(SitePaginationPageNumber(
                    active=objects_page_range_i == page_i,
                    enabled=True,
                    number=objects_page_range_i + 1
                ))
            pagination_builder.visible_page_numbers = tuple(visible_page_numbers)

            pagination = pagination_builder.build()

            pages.append(SitePaginatorPage(
                number_one_based=page_i + 1,
                objects=tuple(objects_chunk),
                pagination=pagination
            ))
        return tuple(pages)

    @staticmethod
    def __page_range(*, page_i, page_max, page_min, window):
        assert window / 2 == window // 2, "window must be even"
        start = page_i - window // 2
        end = page_i + window // 2
        # print("First cut")
        # print(start, end)

        if start >= page_min and end <= page_max:
            return range(start, end + 1)

        # print("Adjusting start")

        while start < page_min:
            start = start + 1
            if end < page_max:
                end = end + 1
            # print(start, end)

        # print("Adjusting end")

        while end > page_max:
            end = end - 1
            if start > page_min:
                start = start - 1
            # print(start, end)

        return range(start, end + 1)
