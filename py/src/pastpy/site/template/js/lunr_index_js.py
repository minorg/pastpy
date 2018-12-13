import json
import os.path
import subprocess
from .._template import _Template


class LunrIndexJs(_Template):
    def render(self):
        args = ["node", os.path.join(self._configuration.output_dir_path, "js", "build_lunr_index.js")]
        result = subprocess.run(args, shell=True, stdout=subprocess.PIPE)
        index_json = result.stdout.decode("utf-8")
        self._render_mustache(
            context={"index_json": index_json},
            out_file_relpath=os.path.join("js", "lunr_index.js"),
            template_name='js/lunr_index.js'
        )
