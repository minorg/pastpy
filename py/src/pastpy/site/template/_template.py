from abc import ABC, abstractmethod
from datetime import datetime
import logging
import os.path
from pastpy.gen.site.template.footer_html_context import FooterHtmlContext
import pystache


class _Template(ABC):
    def __init__(self, *, configuration):
        self._configuration = configuration
        self._footer_html_context = FooterHtmlContext(current_year=datetime.now().year)
        self._logger = logging.getLogger(self.__class__.__name__)

    def _root_relative_href(self, out_dir_relpath):
        return \
            os.path.relpath(
                self._configuration.output_dir_path, os.path.join(self._configuration.output_dir_path, out_dir_relpath)).replace(os.path.sep, '/')

    @abstractmethod
    def render(self):
        pass

    def _render_mustache(self, *, context, out_file_relpath, template_name):
        renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(self._configuration.template_dir_path,)
            )
        rendered = renderer.render_name(template_name, context)
        if out_file_relpath is None:
            out_file_relpath = template_name
        out_file_path = os.path.join(
            self._configuration.output_dir_path, out_file_relpath)
        out_dir_path = os.path.dirname(out_file_path)
        if not os.path.isdir(out_dir_path):
            os.makedirs(out_dir_path)
            self._logger.debug("created directory %s", out_dir_path)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            self._logger.debug("wrote %s", out_file_path)
