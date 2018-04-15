import os.path
from pastpy.gen.site.template.navbar_html_context import NavbarHtmlContext
from pastpy.gen.site.template.search_html_context import SearchHtmlContext
from ._template import _Template


class SearchHtml(_Template):
    def render(self):
        with open(os.path.join(os.path.dirname(__file__), "object_card.html.mustache"), "r") as file_:
            object_card_html_mustache = file_.read()

        self._render_mustache(
            context=SearchHtmlContext(
                configuration=self._configuration,
                footer=self._footer_html_context,
                navbar=NavbarHtmlContext(objects=True),
                object_card_html_mustache=object_card_html_mustache,
                root_relative_href=self._root_relative_href("")
            ),
            out_file_relpath='search.html',
            template_name='search.html'
        )
