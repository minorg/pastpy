import html.parser


class ObjectsListHtmlParser(html.parser.HTMLParser):
    def __init__(self):
        html.parser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        pass
