import unittest

from htmlnode import HMTLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HMTLNode(tag="gurbe", value="girbe", children=["hoi", "doei"], props= {"href" : "https://www.google.nl"}) 
        node2 = HMTLNode(tag="gurbe", value="girbe", children=["hoi", "doei"], props= {"href" : "https://www.google.nl"}) 
        self.assertNotEqual(node, node2)

    def test_tag(self):
        node = HMTLNode(tag="gurbe", value="girbe", children=["hoi", "doei"], props= {"href" : "https://www.google.nl"}) 
        self.assertIsNotNone(node.tag)

    def test_props(self):
        node = HMTLNode(tag="gurbe", value="girbe", children=["hoi", "doei"], props= {"href" : "https://www.google.nl"}) 
        self.assertIsNotNone(node.props)

if __name__ == "__main__":
    unittest.main()
