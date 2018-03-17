from pastpy.impl.online.image import Image
from pastpy.impl.online.image_type import ImageType


class ImageHtmlParser(object):
    def parse(self, image_div_element):
        result_builder = Image.Builder()

        for class_ in image_div_element["class"]:
            if class_ == "indvImage":
                result_builder.type = ImageType.INDIVIDUAL
                break
            elif class_ == "largeImage":
                result_builder.type = ImageType.LARGE
                break
            else:
                continue

        a = image_div_element.a

        result_builder.full_size_url = self.__strip_attr(a.attrs["href"])
        print(result_builder.full_size_url)
        result_builder.src = self.__strip_attr(a.attrs["image_src"])
        result_builder.objectid = self.__strip_attr(a.attrs["objectid"])
        result_builder.mediaid = self.__strip_attr(a.attrs["mediaid"])
        result_builder.thumbnail_url = self.__strip_attr(a.figure.img.attrs["src"])
        result_builder.title = self.__strip_attr(a.attrs["linktitle"])

        return result_builder.build()

    def __strip_attr(self, value):
        old_value = value
        while True:
            for char in "'\\":
                new_value = old_value.strip(char)
                if new_value == old_value:
                    return new_value
                else:
                    old_value = new_value
