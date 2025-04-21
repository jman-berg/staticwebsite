from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_nodes.extend(node)
        delimiter_count = node.text.count(delimiter)
        if delimiter_count % 2 > 0:
            raise Exception("This is not valid markdown, missing a closing delimiter.")
        split_nodes = node.text.split(delimiter)
        
        for index in range(0,len(split_nodes)):
            if index % 2 == 0 and len(split_nodes[index])> 0:
                new_nodes.extend([TextNode(split_nodes[index], TextType.NORMAL)])
            elif len(split_nodes[index]) > 0:
                new_nodes.extend([TextNode(split_nodes[index], text_type)])
    return new_nodes    
