from datetime import date
import logging
import os.path
import shutil
from pastpy.gen.site.site_configuration import SiteConfiguration
from pastpy.site.site_objects_reader import SiteObjectsReader
from pastpy.site.site_paginator import SitePaginator


class SiteGenerator(object):
    TEMPLATE_DIR_PATH_DEFAULT = \
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'template'))
    assert os.path.isdir(
        TEMPLATE_DIR_PATH_DEFAULT), TEMPLATE_DIR_PATH_DEFAULT

    def __init__(self, *, configuration, database):
        assert isinstance(configuration, SiteConfiguration)
        self.__database = database
        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)

        if configuration.template_dir_path is None:
            configuration = configuration.replacer().set_template_dir_path(
                self.TEMPLATE_DIR_PATH_DEFAULT).build()
        if not os.path.isdir(configuration.template_dir_path):
            raise ValueError(
                "template directory %s does not exist" % configuration.template_dir_path)

        self.__configuration = configuration

        self.__objects = None
        self.__objects_pages = None

    def __clean(self):
        self.__rmtree(self.__configuration.output_dir_path)

    def __copy_static_files(self):
        file_paths = {}  # in -> out
        for in_dir_path, _subdir_names, in_file_names in os.walk(self.__configuration.template_dir_path):
            in_dir_relpath = os.path.relpath(in_dir_path, self.__configuration.template_dir_path)
            for in_file_name in in_file_names:
                if in_file_name.endswith(".mustache") or in_file_name.endswith(".py"):
                    continue
                in_file_path = os.path.join(in_dir_path, in_file_name)
                out_dir_path = os.path.join(self.__configuration.output_dir_path, in_dir_relpath)
                out_file_path = os.path.join(out_dir_path, in_file_name)
                file_paths[in_file_path] = out_file_path

        if self.__configuration.theme_css_file_path:
            file_paths[self.__configuration.theme_css_file_path] = os.path.join(self.__configuration.output_dir_path, "css", "theme.css")

        for in_file_path, out_file_path in file_paths.items():
            out_dir_path = os.path.dirname(out_file_path)
            if not os.path.isdir(out_dir_path):
                os.makedirs(out_dir_path)
            shutil.copyfile(in_file_path, out_file_path)
            self.__logger.debug("copied %s to %s",
                                in_file_path, out_file_path)

    def generate(self):
        self.__clean()
        self.__makedirs(self.__configuration.output_dir_path)

        self.__copy_static_files()

        self.__objects = SiteObjectsReader(configuration=self.__configuration, database=self.__database).read_objects()
        self.__objects_pages = tuple(SitePaginator().paginate(objects=self.__objects, objects_per_page=20))

        self.__render_index_html()
        self.__render_object_details_html()
        self.__render_objects_js()
        self.__render_objects_list_html()
        self.__render_sitemap_xml()

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.debug("created directory %s", dir_path)

    def __render_index_html(self):
        from pastpy.site.template.index_html import IndexHtml
        IndexHtml(configuration=self.__configuration).render()

    def __render_object_details_html(self):
        from pastpy.site.template.objects.details.object_detail_html import ObjectDetailHtml
        for object_ in self.__objects:
            ObjectDetailHtml(configuration=self.__configuration, object_=object_).render()

    def __render_objects_js(self):
        from pastpy.site.template.js.objects_js import ObjectsJs
        ObjectsJs(configuration=self.__configuration, objects=self.__objects).render()

    def __render_objects_list_html(self):
        from pastpy.site.template.objects.list.objects_list_html import ObjectsListHtml
        for objects_page in self.__objects_pages:
            ObjectsListHtml(configuration=self.__configuration, objects_page=objects_page).render()

    def __rmtree(self, dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self.__logger.debug("deleted directory %s", dir_path)
