from datetime import datetime
import logging
import os.path
import shutil
import pystache
from urllib.parse import urlparse, unquote
from pastpy.database.past_perfect_database import PastPerfectDatabase
from pastpy.gen.site.site_configuration import SiteConfiguration


class SiteGenerator(object):
    TEMPLATES_DIR_PATH_DEFAULT = \
        os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'templates'))
    assert os.path.isdir(
        TEMPLATES_DIR_PATH_DEFAULT), TEMPLATES_DIR_PATH_DEFAULT

    class ObjectWrapper(object):
        def __init__(self, img_srcs, object_):
            self.__img_srcs = img_srcs
            self.__object = object_

        def __getattr__(self, attr):
            return getattr(self.__object, attr)

        @property
        def img_srcs(self):
            return self.__img_srcs

    def __init__(self, *, configuration):
        assert isinstance(configuration, SiteConfiguration)
        self.__database = PastPerfectDatabase.create(configuration.database)

        self.__logger = logging.getLogger(SiteGenerator.__class__.__name__)

        if configuration.templates_dir_path is None:
            configuration = SiteConfiguration.Builder.from_template(
                configuration).set_templates_dir_path(self.TEMPLATES_DIR_PATH_DEFAULT).build()
        if not os.path.isdir(configuration.templates_dir_path):
            raise ValueError(
                "template directory %s does not exist" % configuration.templates_dir_path)

        self.__configuration = configuration

        self.__renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(configuration.templates_dir_path,)
            )

    def __clean(self):
        self.__rmtree(self.__configuration.output_dir_path)

    def generate(self):
        self.__clean()
        self.__makedirs(self.__configuration.output_dir_path)

        objects = self.__read_objects()

        self.__render_index()
        self.__render_object_details(objects=objects)
        self.__render_objects_list(objects=objects)

    def __makedirs(self, dir_path):
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
            self.__logger.info("created directory %s", dir_path)

    def __new_object_context(self, *, object_):
        return {
            "object": object_,
            "object_attributes": [{"key": key, "value": value} for key, value in object_.attributes.items()]
        }

    def __new_top_level_context(self, *, page_title):
        return {
            'copyright_holder': self.__configuration.copyright_holder,
            'current_year': datetime.now().year,
            'page_title': page_title,
            'site_name': self.__configuration.name
        }

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
            self.__logger.info(
                "created output images directory %s", out_images_dir_path)

        objects = []
        for object_ in self.__database.objects():
            img_srcs = []
            for image in object_.images:
                full_size_url = image.full_size_url
                full_size_url_parsed = urlparse(full_size_url)
                if full_size_url_parsed.scheme == "file":
                    full_size_file_path = unquote(full_size_url)[7:]
                    full_size_file_name = os.path.split(full_size_file_path)[1]
                    out_image_file_path = os.path.join(
                        out_images_dir_path, full_size_file_name)
                    shutil.copyfile(full_size_file_path,
                                    full_size_file_name)
                    self.__logger.info(
                        "copied %s to %s", full_size_file_path, out_image_file_path)
                    img_srcs.append('img/' + full_size_file_name)
            objects.append(SiteGenerator.ObjectWrapper(
                img_srcs=tuple(img_srcs),
                object_=object_
            ))
            if len(objects) == 100:
                break
        return objects

    def __render_file(self, *, context, file_base_name, out_file_relpath=None):
        rendered = self.__renderer.render_name(
            file_base_name + '.html', context)
        if out_file_relpath is None:
            out_file_relpath = file_base_name + '.html'
        out_file_path = os.path.join(
            self.__configuration.output_dir_path, out_file_relpath)
        with open(out_file_path, 'w+') as out_file:
            out_file.write(rendered)
            self.__logger.info("wrote %s", out_file_path)

    def __render_index(self):
        context = self.__new_top_level_context(page_title='Home')
        self.__render_file(context=context, file_base_name='index')

    def __render_object_details(self, *, objects):
        out_dir_relpath = os.path.join('objects', 'details')
        self.__makedirs(os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath))

        for object_ in objects:
            if not object_.id:
                continue
            context = self.__new_top_level_context(
                page_title='Object: ' + object_.id)
            context.update(self.__new_object_context(object_=object_))

            self.__render_file(file_base_name='object_detail', context=context, out_file_relpath=os.path.join(
                out_dir_relpath, object_.id + '.html'))

    def __render_objects_list(self, *, objects):
        out_dir_relpath = os.path.join('objects', 'list')
        self.__makedirs(os.path.join(
            self.__configuration.output_dir_path, out_dir_relpath))

        objects.reverse()
        objects_pages = []
        objects_per_page = 5
        while objects:
            objects_page = []
            while objects and len(objects_page) < objects_per_page:
                object_ = objects.pop()
                if not object_.id:
                    continue
                objects_page.append(object_)
            objects_pages.append(objects_page)

        for objects_page_i, objects_page in enumerate(objects_pages):
            # *page_number* is one-based
            current_page_number = objects_page_i + 1

            context = self.__new_top_level_context(
                page_title='Objects: page ' + str(current_page_number))
            context["objects"] = [self.__new_object_context(
                object_=object_) for object_ in objects_page]

            context["next_page_disabled"] = objects_page_i + 1 == len(objects_pages)
            context["next_page_number"] = objects_page_i + 2
            context["previous_page_disabled"] = objects_page_i == 0
            context["previous_page_number"] = objects_page_i

            page_items = []
            objects_page_range = self.__page_range(page_i=objects_page_i, page_min=0, page_max=len(objects_pages) - 1, window=10)
            print(objects_page_range)
            for objects_page_range_i in objects_page_range:
                page_items.append({"active": objects_page_range_i ==
                                   objects_page_i, "number": objects_page_range_i + 1})
            context["page_items"] = page_items

            self.__render_file(file_base_name='objects_list', context=context, out_file_relpath=os.path.join(
                out_dir_relpath, str(objects_page_i + 1) + '.html'))

    def __rmtree(self, dir_path):
        if os.path.isdir(dir_path):
            shutil.rmtree(dir_path)
            self.__logger.info("deleted directory %s", dir_path)
