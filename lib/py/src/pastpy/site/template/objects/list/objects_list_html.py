from ..._template import _Template
import os.path
from pastpy.gen.site.site_objects_list import SiteObjectsList


class ObjectsListHtml(_Template):
    def __init__(self, *, objects_page, **kwds):
        _Template.__init__(self, **kwds)
        self.__objects_page = objects_page

    def render(self):
        out_dir_relpath = os.path.join('objects', 'list')
        out_file_relpath = os.path.join(
            out_dir_relpath, str(self.__objects_page.number_one_based) + '.html')

        context_builder = SiteObjectsList.builder()
        context_builder.absolute_href = "/" + \
            out_file_relpath.replace(os.path.sep, '/')
        context_builder.metadata = self._new_metadata(
            active_nav_item="objects", out_dir_relpath=out_dir_relpath)
        context_builder.objects = self.__objects_page.objects
        context_builder.pagination = self.__objects_page.pagination
        context = context_builder.build()

        self._render_mustache(
            context=context,
            out_file_relpath=out_file_relpath,
            template_name='objects/list/objects_list.html'
        )
