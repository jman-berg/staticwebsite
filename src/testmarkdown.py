import unittest

from markdownparser import markdown_to_blocks, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links, text_to_textnodes, markdown_to_html_node
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

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
              [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md.strip())
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md.strip())
        html = node.to_html()
        print(html)
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

