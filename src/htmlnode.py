class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        html_string = ""
        for k,v in self.props.items():
            html_string += f' {k}="{v}"'
        return html_string

    def __repr__(self):
        return f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"
        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None ):
        super().__init__(tag, value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        
        if self.tag is None:
            return self.value

        props_html = self.props_to_html() if self.props else ""
        
        return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if  self.children is None:
            raise ValueError("ParentNode must have children")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += child.to_html()
        return html_string + f"</{self.tag}>"










