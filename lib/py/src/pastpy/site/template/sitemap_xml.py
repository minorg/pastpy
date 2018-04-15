from datetime import date
from ._template import _Template
from pastpy.gen.site.site_pagination_page_number import SitePaginationPageNumber
from pastpy.gen.site.site_sitemap import SiteSitemap


class SitemapXml(_Template):
    def __init__(self, *, objects, objects_pages, **kwds):
        _Template.__init__(self, **kwds)
        self.__objects = objects
        self.__objects_pages = objects_pages

    def render(self):
        context_builder = SiteSitemap.builder()
        context_builder.configuration = self._configuration
        context_builder.lastmod = date.today().isoformat()
        context_builder.objects_list_page_numbers = tuple(SitePaginationPageNumber(active=True, enabled=True, number=objects_page.number_one_based) for objects_page in self.__objects_pages)
        objects = []
        for object_ in self.__objects:
            objects.append(object_.replacer().set_standard_attributes_list_xml(tuple(
                item for item in object_.standard_attributes_list_xml
                if item.name != "description"
            )).build())
        context_builder.objects = tuple(objects)
        context = context_builder.build()

        self._render_mustache(
            context=context,
            out_file_relpath='sitemap.xml',
            template_name='sitemap.xml'
        )
