from ..._template import _Template
import os.path
from pastpy.gen.site.site_object_detail import SiteObjectDetail


class ObjectDetailHtml(_Template):
    def __init__(self, *, object_, **kwds):
        _Template.__init__(self, **kwds)
        self.__object = object_

    def render(self):
        out_dir_relpath = os.path.join('objects', 'details')
        context = \
            SiteObjectDetail(
                metadata=self._new_metadata(
                    active_nav_item="objects",
                    out_dir_relpath=out_dir_relpath
                ),
                object=self.__object
            )
        self._render_mustache(
            context=context,
            out_file_relpath=os.path.join(out_dir_relpath, context.object.file_name),
            template_name='objects/details/object_detail.html'
        )
