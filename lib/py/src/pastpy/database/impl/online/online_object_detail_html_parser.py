from bs4 import BeautifulSoup

from pastpy.gen.database.impl.online.online_object_detail import OnlineObjectDetail
from pastpy.impl.online.online_image_html_parser import OnlineImageHtmlParser


class OnlineObjectDetailHtmlParser(object):
    def parse(self, *, guid, html):
        image_parser = OnlineImageHtmlParser()
        soup = BeautifulSoup(html, "html.parser")
        result_builder = OnlineObjectDetail.Builder()

        result_builder.guid = guid

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
        result_builder.attributes = attributes

        related_photos_element = soup.find(attrs={"class": "relatedPhotos"})
        related_photos = []
        if related_photos_element:
            for td in related_photos_element.find_all("td"):
                related_photos.append(image_parser.parse(td.div))
        result_builder.related_photos = tuple(related_photos)

        return result_builder.build()
