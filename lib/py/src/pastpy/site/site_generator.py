from collections import OrderedDict
from datetime import date, datetime
import logging
import os.path
import re
import shutil
import pystache
import inspect
from urllib.parse import urlparse, unquote
from pastpy.gen.site.site_configuration import SiteConfiguration


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

        self.__renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(configuration.template_dir_path,)
            )

    def __clean(self):
        self.__rmtree(self.__configuration.output_dir_path)

    def __copy_static_files(self):
        for dir_name in ("css", "js"):
            src_dir_path = os.path.join(
                self.__configuration.template_dir_path, dir_name)
            if os.path.isdir(src_dir_path):
                dst_dir_path = os.path.join(
                    self.__configuration.output_dir_path, dir_name)
                shutil.copytree(src_dir_path, dst_dir_path)
                self.__logger.debug("copied %s to %s",
                                    src_dir_path, dst_dir_path)

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

        objects = self.__read_objects()
        objects = self.__filter_objects_with_ids(objects=objects)

        object_file_names_by_id = self.__map_objects_to_file_names(
            objects=objects)

        self.__render_index()
        self.__render_object_details(
            object_file_names_by_id=object_file_names_by_id, objects=objects,)
        self.__render_objects_list(
            object_file_names_by_id=object_file_names_by_id, objects=objects)
        self.__render_sitemap(
            object_file_names_by_id=object_file_names_by_id, objects=objects)

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.debug("created directory %s", dir_path)

    def __map_objects_to_file_names(self, *, objects):
        object_ids_by_file_name = {}
        file_names_by_object_id = {}
        for object_ in objects:
            file_name = self.__to_valid_filename(object_.id) + ".html"
            existing_object_id = object_ids_by_file_name.get(file_name)
            if existing_object_id is not None:
                raise RuntimeError("two objects (%s and %s) map to the same file name (%s)" % (
                    existing_object_id, object_.id, file_name))
            object_ids_by_file_name[file_name] = object_.id
            file_names_by_object_id[object_.id] = file_name
        return file_names_by_object_id

    def __new_object_context(self, *, object_, object_file_name):
        context = {}

        context["absolute_href"] = "/objects/details/" + object_file_name
        context["file_name"] = object_file_name
        context["relative_href"] = "../details/" + object_file_name

        context["impl_attributes"] = [{"key": key, "value": value}
                                      for key, value in object_.impl_attributes.items()]

        context["full_size_images"] = [
            image for image in object_.images if image.full_size_url]
        context["has_full_size_images"] = len(context["full_size_images"]) > 0

        if object_.name:
            context["name"] = object_.name
        elif object_.othername:
            context["name"] = object_.othername
        else:
            context["name"] = object_.id

        standard_attributes = {}
        for member_name, member in inspect.getmembers(object_):
            if inspect.ismethod(member):
                continue
            if member_name.startswith('_'):
                continue
            elif member_name in ("images", "impl_attributes"):
                continue
            value = getattr(object_, member_name)
            if value is not None:
                standard_attributes[member_name] = value
        context["standard_attributes"] = [
            {"key": key, "value": value} for key, value in standard_attributes.items()]
        context.update(standard_attributes)

        context["thumbnail_images"] = [
            image for image in object_.images if image.thumbnail_url]
        context["has_thumbnail_images"] = len(context["thumbnail_images"]) > 0
        context["thumbnail_url"] = "http://via.placeholder.com/210x211?text=Missing%20image"
        for image in object_.images:
            if image.thumbnail_url:
                context["thumbnail_url"] = image.thumbnail_url
                break

        if "title" not in context:
            context["title"] = context["name"]

        return {"object": context}

    def __new_top_level_context(self, *, out_dir_path):
        root_rel_href = os.path.relpath(
            self.__configuration.output_dir_path, out_dir_path).replace(os.path.sep, '/')
        context = \
            {
                'current_year': datetime.now().year,
                'home_nav_item_active': False,
                'objects_nav_item_active': False,
                'root_rel_href': root_rel_href,
                'site_name': self.__configuration.name
            }
        context.update(self.__configuration.to_builtins())
        del context["name"]  # Already site_name
        return context

    @staticmethod
    def __page_range(*, page_i, page_max, page_min, window):
        assert window / 2 == window // 2, "window must be even"
        start = page_i - window // 2
        end = page_i + window // 2
        # print("First cut")
        # print(start, end)

        if start >= page_min and end <= page_max:
            return range(start, end + 1)

        # print("Adjusting start")

        while start < page_min:
            start = start + 1
            if end < page_max:
                end = end + 1
            # print(start, end)

        # print("Adjusting end")

        while end > page_max:
            end = end - 1
            if start > page_min:
                start = start - 1
            # print(start, end)

        return range(start, end + 1)

    def __read_objects(self):
        out_images_dir_path = os.path.join(
            self.__configuration.output_dir_path, 'img')
        if not os.path.isdir(out_images_dir_path):
            os.makedirs(out_images_dir_path)
            self.__logger.debug(
                "created output images directory %s", out_images_dir_path)

        objects = []
        for object_ in self.__database.objects():
            for image in object_.images:
                full_size_url = image.full_size_url
                full_size_url_parsed = urlparse(full_size_url)
                if full_size_url_parsed.scheme == "file":
                    raise NotImplementedError(
                        "TODO: rewrite the actual image object with a substitute")
                    # full_size_file_path = unquote(full_size_url)[7:]
                    # full_size_file_name = os.path.split(full_size_file_path)[1]
                    # out_image_file_path = os.path.join(
                    #     out_images_dir_path, full_size_file_name)
                    # shutil.copyfile(full_size_file_path,
                    #                 full_size_file_name)
                    # self.__logger.debug(
                    #     "copied %s to %s", full_size_file_path, out_image_file_path)
                    # img_srcs.append('img/' + full_size_file_name)
            objects.append(object_)
            if len(objects) == 100:
                break
        return objects

    def __render_file(self, *, context, file_name, out_file_relpath=None):
        rendered = self.__renderer.render_name(
            file_name, context)
        if out_file_relpath is None:
            out_file_relpath = file_name
        out_file_path = os.path.join(
            self.__configuration.output_dir_path, out_file_relpath)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            self.__logger.debug("wrote %s", out_file_path)

    def __render_index(self):
        context = \
            self.__new_top_level_context(
                out_dir_path=self.__configuration.output_dir_path
            )
        context["home_nav_item_active"] = True
        self.__render_file(context=context, file_name='index.html')

    def __render_object_details(self, *, object_file_names_by_id, objects):
        out_dir_relpath = os.path.join('objects', 'details')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        for object_ in objects:
            object_file_name = object_file_names_by_id[object_.id]
            context = \
                self.__new_top_level_context(
                    out_dir_path=out_dir_path
                )
            context.update(self.__new_object_context(
                object_=object_,
                object_file_name=object_file_name
            ))
            self.__render_file(file_name='object_detail.html', context=context, out_file_relpath=os.path.join(
                out_dir_relpath, object_file_name))

    def __render_objects_list(self, *, object_file_names_by_id, objects):
        out_dir_relpath = os.path.join('objects', 'list')
        out_dir_path = os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath)
        self.__makedirs(out_dir_path)

        objects = list(reversed(objects))
        objects_pages = []
        objects_per_page = 20
        while objects:
            objects_page = []
            while objects and len(objects_page) < objects_per_page:
                object_ = objects.pop()
                objects_page.append(object_)
            objects_pages.append(objects_page)

        for objects_page_i, objects_page in enumerate(objects_pages):
            # *page_number* is one-based
            current_page_number = objects_page_i + 1

            context = \
                self.__new_top_level_context(
                    out_dir_path=out_dir_path
                )
            context["objects"] = \
                [self.__new_object_context(
                    object_=object_,
                    object_file_name=object_file_names_by_id[object_.id])
                 for object_ in objects_page]
            context["objects_nav_item_active"] = True
            context["next_page_disabled"] = objects_page_i + \
                1 == len(objects_pages)
            context["next_page_number"] = objects_page_i + 2
            context["previous_page_disabled"] = objects_page_i == 0
            context["previous_page_number"] = objects_page_i

            page_items = []
            objects_page_range = self.__page_range(
                page_i=objects_page_i, page_min=0, page_max=len(objects_pages) - 1, window=10)
            for objects_page_range_i in objects_page_range:
                page_items.append({"active": objects_page_range_i ==
                                   objects_page_i, "number": objects_page_range_i + 1})
            context["page_items"] = page_items

            self.__render_file(
                file_name='objects_list.html',
                context=context,
                out_file_relpath=os.path.join(
                    out_dir_relpath, str(objects_page_i + 1) + '.html')
            )

    def __render_sitemap(self, *, object_file_names_by_id, objects):
        object_contexts = []
        for object_ in objects:
            object_file_name = object_file_names_by_id[object_.id]
            object_context = \
                self.__new_top_level_context(
                    out_dir_path=self.__configuration.output_dir_path
                )
            object_context.update(self.__new_object_context(
                object_=object_,
                object_file_name=object_file_name
            ))
            object_context["object"]["standard_attributes"] = [item for item in object_context["object"]["standard_attributes"] if item["key"] != "description"]
            object_contexts.append(object_context)
        context = {"objects": object_contexts}
        context["lastmod"] = date.today().isoformat()
        self.__render_file(file_name='sitemap.xml', context=context)

    def __rmtree(self, dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self.__logger.debug("deleted directory %s", dir_path)

    @staticmethod
    def __to_valid_filename(s):
        s = str(s).strip().replace(' ', '_')
        return re.sub(r'(?u)[^-\w.]', '', s)
