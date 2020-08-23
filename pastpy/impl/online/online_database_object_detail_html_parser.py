from bs4 import BeautifulSoup, Tag

from pastpy.impl.online.online_database_object_detail import OnlineDatabaseObjectDetail
from pastpy.impl.online.online_database_object_detail_image import (
    OnlineDatabaseObjectDetailImage,
)
from pastpy.impl.online.online_database_object_detail_image_type import (
    OnlineDatabaseObjectDetailImageType,
)


class OnlineDatabaseObjectDetailHtmlParser:
    def parse(self, *, guid: str, html: str) -> OnlineDatabaseObjectDetail:
        soup = BeautifulSoup(html, "html.parser")

        result_kwds = {}

        result_kwds["guid"] = guid

        attributes = {}
        for category_element in soup.find(attrs={"class": "recordData"}).find_all(
            attrs={"class": "category"}
        ):
            category_string = "".join(category_element.stripped_strings).strip()
            display_element = category_element.parent.find(attrs={"class": "display"})
            if not display_element:
                continue
            display_strings = []
            for page_element in display_element.contents:
                if isinstance(page_element, str):
                    display_string = page_element
                else:
                    assert isinstance(page_element, Tag)
                    if page_element.name == "br":
                        continue
                    if page_element.name != "a":
                        # Something that looks like a tag that isn't, like unescaped <whatever>
                        continue
                    # Use the link text
                    display_string = "".join(page_element.stripped_strings)
                display_string = (
                    display_string.replace("\\n", "").replace("\\'", "'").strip()
                )
                if not display_string:
                    continue
                display_strings.append(display_string)
            if not category_string or not display_strings:
                continue
            if category_string == "Object ID":
                assert "id" not in result_kwds
                result_kwds["id"] = (
                    display_strings[0]
                    if len(display_strings) == 1
                    else tuple(display_strings)
                )
            else:
                assert category_string not in attributes
                attributes[category_string] = (
                    display_strings[0]
                    if len(display_strings) == 1
                    else tuple(display_strings)
                )
        result_kwds["attributes"] = attributes

        related_photos_element = soup.find(attrs={"class": "relatedPhotos"})
        related_photos = []
        if related_photos_element:
            for td in related_photos_element.find_all("td"):
                related_photos.append(self.__parse_image(td.div))
        result_kwds["related_photos"] = tuple(related_photos)

        return OnlineDatabaseObjectDetail(**result_kwds)

    def __parse_image(self, image_div_element) -> OnlineDatabaseObjectDetailImage:

        type_ = None
        for class_ in image_div_element["class"]:
            if class_ == "indvImage":
                type_ = OnlineDatabaseObjectDetailImageType.INDIVIDUAL
                break
            elif class_ == "largeImage":
                type_ = OnlineDatabaseObjectDetailImageType.LARGE
                break
            else:
                continue

        a = image_div_element.a

        return OnlineDatabaseObjectDetailImage(
            full_size_url=self.__strip_attr(a.attrs["href"]),
            mediaid=self.__strip_attr(a.attrs["mediaid"]),
            objectid=self.__strip_attr(a.attrs["objectid"]),
            src=self.__strip_attr(a.attrs["image_src"]),
            thumbnail_url=self.__strip_attr(a.figure.img.attrs["src"]),
            title=self.__strip_attr(a.attrs["linktitle"]),
            type=type_,
        )

    def __strip_attr(self, value):
        old_value = value
        while True:
            for char in "'\\":
                new_value = old_value.strip(char)
                if new_value == old_value:
                    return new_value
                else:
                    old_value = new_value
