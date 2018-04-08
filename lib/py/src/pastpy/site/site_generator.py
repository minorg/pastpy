from collections import OrderedDict
from datetime import date, datetime
import logging
import os.path
import shutil
import pystache
from pastpy.gen.site.site_configuration import SiteConfiguration
from pastpy.gen.site.site_index import SiteIndex
from pastpy.gen.site.site_metadata import SiteMetadata
from pastpy.gen.site.site_nav_items import SiteNavItems
from pastpy.gen.site.site_object_detail import SiteObjectDetail
from pastpy.gen.site.site_objects_list import SiteObjectsList
from pastpy.gen.site.site_objects_list_page_number import SiteObjectsListPageNumber
from pastpy.gen.site.site_sitemap import SiteSitemap
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

        self.__renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(configuration.template_dir_path,)
            )

    def __clean(self):
        self.__rmtree(self.__configuration.output_dir_path)

    def __copy_static_files(self):
        file_paths = {}
        for in_dir_path, subdir_names, in_file_names in os.walk(self.__configuration.template_dir_path):
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

    def __filter_objects_with_ids(self, *, objects):
        objects_by_id = OrderedDict()
        for object_ in objects:
            if object_.id:
                if object_.id not in objects_by_id:
                    objects_by_id[object_.id] = object_
                else:
                    self.__logger.warning("duplicate object id: %s", object_)
            else:
                self.__logger.warning("object has no id: %s", object_)
        return objects_by_id.values()

    def generate(self):
        self.__clean()
        self.__makedirs(self.__configuration.output_dir_path)

        self.__copy_static_files()

        self.__objects = SiteObjectsReader(configuration=self.__configuration, database=self.__database).read_objects()

        self.__render_index()
        self.__render_object_details()
        objects_list_pages = self.__render_objects_list()
        self.__render_sitemap(objects_list_pages=objects_list_pages)

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.debug("created directory %s", dir_path)

    def __new_metadata(self, *, out_dir_path, active_nav_item="home"):
        builder = SiteMetadata.builder()
        builder.root_relative_href = os.path.relpath(
            self.__configuration.output_dir_path, out_dir_path).replace(os.path.sep, '/')
        builder.configuration = self.__configuration
        builder.current_year = datetime.now().year
        nav_items_builder = SiteNavItems.builder()
        setattr(nav_items_builder, active_nav_item, True)
        builder.nav_items = nav_items_builder.build()
        return builder.build()

    def __render_file(self, *, context, out_file_relpath, template_name):
        rendered = self.__renderer.render_name(template_name, context)
        if out_file_relpath is None:
            out_file_relpath = template_name
        out_file_path = os.path.join(
            self.__configuration.output_dir_path, out_file_relpath)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            self.__logger.debug("wrote %s", out_file_path)

    def __render_index(self):
        context = \
            SiteIndex(
                has_featured_searches=bool(self.__configuration.featured_searches),
                metadata=self.__new_metadata(
                    active_nav_item="home",
                    out_dir_path=self.__configuration.output_dir_path
                )
            )
        self.__render_file(
            context=context,
            out_file_relpath='index.html',
            template_name='index.html'
        )

    def __render_object_details(self):
        out_dir_relpath = os.path.join('objects', 'details')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        for object_ in self.__objects:
            context = \
                SiteObjectDetail(
                    metadata=self.__new_metadata(
                        active_nav_item="objects",
                        out_dir_path=out_dir_path
                    ),
                    object=object_
                )
            self.__render_file(
                context=context,
                out_file_relpath=os.path.join(out_dir_relpath, context.object.file_name),
                template_name='objects/details/object_detail.html'
            )

    def __render_objects_list(self):
        out_dir_relpath = os.path.join('objects', 'list')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        objects_list_pages = []
        for page in SitePaginator().paginate(objects=self.__objects, objects_per_page=20):
            out_file_relpath = os.path.join(
                out_dir_relpath, str(page.number_one_based) + '.html')

            context_builder = SiteObjectsList.builder()
            context_builder.absolute_href = "/" + \
                out_file_relpath.replace(os.path.sep, '/')
            context_builder.metadata = self.__new_metadata(
                active_nav_item="objects", out_dir_path=out_dir_path)
            context_builder.objects = page.objects
            context_builder.pagination = page.pagination
            context = context_builder.build()

            self.__render_file(
                context=context,
                out_file_relpath=out_file_relpath,
                template_name='objects/list/objects_list.html'
            )
            objects_list_pages.append(context)
        return tuple(objects_list_pages)

    def __render_sitemap(self, objects_list_pages):
        context_builder = SiteSitemap.builder()
        context_builder.configuration = self.__configuration
        context_builder.lastmod = date.today().isoformat()
        context_builder.objects_list_pages = objects_list_pages
        objects = []
        for object_ in self.__objects:
            objects.append(object_.replacer().set_standard_attributes_list_xml(tuple(
                item for item in object_.standard_attributes_list_xml
                if item.name != "description"
            )).build())
        context_builder.objects = tuple(objects)
        context = context_builder.build()

        self.__render_file(
            context=context,
            out_file_relpath='sitemap.xml',
            template_name='sitemap.xml'
        )

    def __rmtree(self, dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self.__logger.debug("deleted directory %s", dir_path)
