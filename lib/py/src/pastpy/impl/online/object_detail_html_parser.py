from bs4 import BeautifulSoup

from pastpy.impl.online.image_html_parser import ImageHtmlParser
from pastpy.impl.online.object_detail import ObjectDetail


class ObjectDetailHtmlParser(object):
    def parse(self, html):
        image_parser = ImageHtmlParser()
        soup = BeautifulSoup(html, "html.parser")
        result_builder = ObjectDetail.Builder()

        related_photos = soup.find(attrs={"class": "relatedPhotos"})
        if related_photos:
            images = []
            for td in related_photos.find_all("td"):
                images.append(image_parser.parse(td.div))
            if images:
                result_builder.related_photos = tuple(images)

        return result_builder.build()
