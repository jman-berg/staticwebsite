class HMTLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

        def to_html(self):
            raise NotImplementedError()

        def props_to_html(self):
            html_string = ""
            for k,v in self.props:
                html_string += f' {k}="{v}"'
            return html_string

        def __repr__(self):
            return f"tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"


