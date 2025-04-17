from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
        def __init__(self, TEXT, TEXT_TYPE, URL):
            self.text = TEXT
            self.text_type = TEXT_TYPE
            self.url = URL

        def __eq__(self, other):
            return self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url

        def __repr__(self):
            return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


            

