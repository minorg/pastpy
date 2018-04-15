from pastpy.gen.site.site_index import SiteIndex
from ._template import _Template


class IndexHtml(_Template):
    def render(self):
        context = \
            SiteIndex(
                has_featured_searches=bool(self._configuration.featured_searches),
                metadata=self._new_metadata(
                    active_nav_item="home",
                    out_dir_relpath=""
                )
            )
        self._render_mustache(
            context=context,
            out_file_relpath='index.html',
            template_name='index.html'
        )
