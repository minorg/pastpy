from ..._template import _Template
import os.path
from pastpy.gen.site.template.navbar_html_context import NavbarHtmlContext
from pastpy.gen.site.template.objects.detail.object_detail_html_context import ObjectDetailHtmlContext


class ObjectDetailHtml(_Template):
    def __init__(self, *, object_, **kwds):
        _Template.__init__(self, **kwds)
        self.__object = object_

    def render(self):
        out_dir_relpath = os.path.join('objects', 'details')
        context = \
            ObjectDetailHtmlContext(
                configuration=self._configuration,
                footer=self._footer_html_context,
                navbar=NavbarHtmlContext(objects=True),
                object=self.__object,
                root_relative_href=self._root_relative_href(out_dir_relpath=out_dir_relpath)
            )
        self._render_mustache(
            context=context,
            out_file_relpath=os.path.join(out_dir_relpath, context.object.file_name),
            template_name='objects/details/object_detail.html'
        )
