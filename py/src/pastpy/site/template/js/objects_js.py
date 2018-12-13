import json
import os.path
from .._template import _Template


class ObjectsJs(_Template):
    def __init__(self, *, objects, **kwds):
        _Template.__init__(self, **kwds)
        self.__objects = objects

    def render(self):
        objects_json = {}
        for object_ in self.__objects:
            object_json = object_.standard_attributes_map.copy()
            object_json["absolute_href"] = object_.absolute_href
            object_json["thumbnail_url"] = object_.thumbnail_url
            objects_json[object_.id] = object_json
        self._render_mustache(
            context={"objects_json": json.dumps(objects_json)},
            out_file_relpath=os.path.join("js", "objects.js"),
            template_name='js/objects.js'
        )
