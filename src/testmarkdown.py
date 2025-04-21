import unittest

from markdownparser import split_nodes_delimiter
from textnode import TextNode, TextType

class TestParser(unittest.TestCase):

    def test_list(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIsInstance(new_node, list)
    
    def test_bold(self):
        node = TextNode("This is text with a **code block** word", TextType.NORMAL)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node[1].text_type, TextType.BOLD)
        
    def test_italic(self):
        node = TextNode("This is text with a _code block_ word", TextType.NORMAL)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_node[1].text_type, TextType.ITALIC)


