from bs4 import BeautifulSoup

from pastpy.impl.online.image_html_parser import ImageHtmlParser
from pastpy.impl.online.object_detail import ObjectDetail


class ObjectDetailHtmlParser(object):
    def parse(self, *, guid, html):
        image_parser = ImageHtmlParser()
        soup = BeautifulSoup(html, "html.parser")
        result_builder = ObjectDetail.Builder()

        result_builder.guid = guid

        related_photos = soup.find(attrs={"class": "relatedPhotos"})
        if related_photos:
            images = []
            for td in related_photos.find_all("td"):
                images.append(image_parser.parse(td.div))
            if images:
                result_builder.related_photos = tuple(images)

        attributes = {}
        for category_element in soup.find(attrs={"class": "recordData"}).find_all(attrs={"class": "category"}):
            category_string = ''.join(category_element.stripped_strings).strip()
            display_element = category_element.parent.find(attrs={"class": "display"})
            if not display_element:
                continue
            display_string = ''.join(display_element.stripped_strings).replace("\\n", '').strip()
            if not category_string or not display_string:
                continue
            if category_string == "Object ID":
                assert result_builder.id is None
                result_builder.id = display_string
            else:
                assert category_string not in attributes
                attributes[category_string] = display_string
        if attributes:
            result_builder.attributes = attributes

        return result_builder.build()
