from ..._template import _Template
import os.path
from pastpy.gen.site.template.navbar_html_context import NavbarHtmlContext
from pastpy.gen.site.template.objects.list.objects_list_html_context import ObjectsListHtmlContext


class ObjectsListHtml(_Template):
    def __init__(self, *, objects_page, **kwds):
        _Template.__init__(self, **kwds)
        self.__objects_page = objects_page

    def render(self):
        out_dir_relpath = os.path.join('objects', 'list')
        out_file_relpath = os.path.join(
            out_dir_relpath, str(self.__objects_page.number_one_based) + '.html')

        context_builder = ObjectsListHtmlContext.builder()
        context_builder.absolute_href = "/" + \
            out_file_relpath.replace(os.path.sep, '/')
        context_builder.configuration = self._configuration
        context_builder.footer = self._footer_html_context
        context_builder.objects = self.__objects_page.objects
        context_builder.navbar = NavbarHtmlContext(objects=True)
        context_builder.pagination = self.__objects_page.pagination
        context_builder.root_relative_href = self._root_relative_href(out_dir_relpath=out_dir_relpath)
        context = context_builder.build()

        self._render_mustache(
            context=context,
            out_file_relpath=out_file_relpath,
            template_name='objects/list/objects_list.html'
        )
