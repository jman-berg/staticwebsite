import unittest

from textnode import TextNode, TextType


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




        


if __name__ == "__main__":
    unittest.main()
