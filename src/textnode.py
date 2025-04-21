from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
        def __init__(self, TEXT, TEXT_TYPE, URL = None):
            self.text = TEXT
            self.text_type = TEXT_TYPE
            self.url = URL

        def __eq__(self, other):
            return self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url

        def __repr__(self):
            return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
        case TextType.IMAGE: 
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt" : "alt text"})
        case _:
            raise Exception("Not a valid TextType")



