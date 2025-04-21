import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("That is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_nourl(self):
        node = TextNode("That is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_texttype(self):
        node = TextNode("That is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_url_eq(self):
        node = TextNode("That is a text node", TextType.NORMAL, "url1")
        node2 = TextNode("This is a text node", TextType.BOLD, "url2")
        self.assertNotEqual(node.url, node2.url)

class TestTextNodeToHTML(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

if __name__ == "__main__":
    unittest.main()
