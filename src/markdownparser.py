from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_nodes.extend([node])
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

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            return new_nodes.extend([node])
        
        for anchor_text, url in links:
            sections = original_text.split(f"[{anchor_text}]({url})",1)
            text_node = TextNode(TEXT=sections[0], TEXT_TYPE=TextType.NORMAL)
            if text_node.text != "":
                new_nodes.extend([text_node])
            link_node = TextNode(TEXT=anchor_text, TEXT_TYPE=TextType.LINK, URL=url)
            if link_node.text != "":
                new_nodes.extend([link_node])
            original_text = sections[1]
        return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_images(original_text)

        if len(links) == 0:
            return new_nodes.extend([node])
        
        for image_alt, image_link in links:
            sections = original_text.split(f"![{image_alt}]({image_link})",1)
            text_node = TextNode(TEXT=sections[0], TEXT_TYPE=TextType.NORMAL)
            if text_node.text != "":
                new_nodes.extend([text_node])
            link_node = TextNode(TEXT=image_alt, TEXT_TYPE=TextType.IMAGE, URL=image_link)
            if link_node.text != "":
                new_nodes.extend([link_node])
            original_text = sections[1]
    return new_nodes

