from pastpy.gen.site.template.index_html_context import IndexHtmlContext
from pastpy.gen.site.template.navbar_html_context import NavbarHtmlContext
from ._template import _Template


class IndexHtml(_Template):
    def render(self):
        context = \
            IndexHtmlContext(
                configuration=self._configuration,
                footer=self._footer_html_context,
                has_featured_searches=bool(self._configuration.featured_searches),
                navbar=NavbarHtmlContext(home=True),
                root_relative_href=self._root_relative_href(out_dir_relpath="")
            )
        self._render_mustache(
            context=context,
            out_file_relpath='index.html',
            template_name='index.html'
        )
