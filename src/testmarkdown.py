import unittest

from markdownparser import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links
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

class TestMarkdownImagesAndLinks(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with an [url](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("url", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestSplitnodes(unittest.TestCase):

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
           new_nodes 
        )

    def test_split_links(self):

        node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)

        new_nodes = split_nodes_links([node])
        
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
            ],
            new_nodes 
        )
