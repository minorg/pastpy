import json
import os.path
from .._template import _Template


class ObjectsJs(_Template):
    def __init__(self, *, objects, **kwds):
        _Template.__init__(self, **kwds)
        self.__objects = objects

    def render(self):
        self._render_mustache(
            context={"objects_json": json.dumps([object_.standard_attributes_map for object_ in self.__objects])},
            out_file_relpath=os.path.join("js", "objects.js"),
            template_name='js/objects.js'
        )
