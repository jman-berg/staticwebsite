from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from blocktypes import block_to_block_type, BlockType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_nodes.extend([node])
            continue
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
            new_nodes.extend([node])
            continue

        for anchor_text, url in links:
            sections = original_text.split(f"[{anchor_text}]({url})",1)
            text_node = TextNode(TEXT=sections[0], TEXT_TYPE=TextType.NORMAL)
            if text_node.text != "":
                new_nodes.extend([text_node])
            link_node = TextNode(TEXT=anchor_text, TEXT_TYPE=TextType.LINK, URL=url)
            if link_node.text != "":
                new_nodes.extend([link_node])
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes


def split_nodes_images(old_nodes):
    new_nodes = []

    for node in old_nodes:
        original_text = node.text
        links = extract_markdown_images(original_text)

        if len(links) == 0:
            new_nodes.extend([node])
            continue
        
        for image_alt, image_link in links:
            sections = original_text.split(f"![{image_alt}]({image_link})",1)
            text_node = TextNode(TEXT=sections[0], TEXT_TYPE=TextType.NORMAL)
            if text_node.text != "":
                new_nodes.extend([text_node])
            link_node = TextNode(TEXT=image_alt, TEXT_TYPE=TextType.IMAGE, URL=image_link)
            if link_node.text != "":
                new_nodes.extend([link_node])
            original_text = sections[1]
        if original_text:
            new_nodes.append(TextNode(original_text, TextType.NORMAL))
    return new_nodes

def text_to_textnodes(text):
    original_text_node = [TextNode(TEXT=text, TEXT_TYPE=TextType.NORMAL)]
    text_split_bold = split_nodes_delimiter(original_text_node, "**", TextType.BOLD)
    text_split_italic = split_nodes_delimiter(text_split_bold, "_", TextType.ITALIC)
    text_split_code = split_nodes_delimiter(text_split_italic, "`", TextType.CODE)
    text_split_links = split_nodes_links(text_split_code)
    text_split_images = split_nodes_images(text_split_links)
    return text_split_images 

def markdown_to_blocks(markdown):
    raw_block_strings = markdown.split("\n\n")
    stripped_strings = []
    for string in raw_block_strings:
        if len(string) != 0:
            stripped_strings.append(string.strip())
    return stripped_strings

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                stripped_block = block.strip("`").lstrip()
                text_node = TextNode(TEXT=stripped_block, TEXT_TYPE=TextType.CODE)
                html_node = text_node_to_html_node(text_node)
                pre_tag_node = ParentNode(tag="pre", children=[html_node])
                html_nodes.append(pre_tag_node)
            case BlockType.PARAGRAPH:
                children = text_to_children(block)
                parent_node = ParentNode(tag="p", children=children)
                html_nodes.append(parent_node)
            case BlockType.HEADING:
                no_hekkies = block.count("#")
                stripped_block = block.strip("#")
                children = text_to_children(stripped_block)
                parent_node = ParentNode(tag=f"h{no_hekkies}", children=children)
                html_nodes.append(parent_node)
            case BlockType.QUOTE:
                children = text_to_children(block)
                parent_node = ParentNode(tag="blockquote", children=children)
                html_nodes.append(parent_node)
            case BlockType.UNORDERED_LIST:
                li_block = split_lists(block)
                children = text_to_children(li_block)
                parent_node = ParentNode(tag="ul", children=children)
                html_nodes.append(parent_node)
            case BlockType.ORDERED_LIST:
                li_block = split_lists(block)
                children = text_to_children(li_block)
                parent_node = ParentNode(tag="ol", children=children)
                html_nodes.append(parent_node)


    return ParentNode(tag="div", children=html_nodes)
            


def text_to_children(text):
    text_without_newlines = " ".join(text.splitlines())
    text_nodes = text_to_textnodes(text_without_newlines)
    html_nodes = []
    for node in text_nodes:
        html_node= text_node_to_html_node(node)
        html_nodes.append(html_node)
    return html_nodes

def split_lists(text):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        stripped_line = line.strip("- ")
        new_line = f"<li>{stripped_line}</li>"
        new_lines.append(new_line)
        new_text = "\n".join(new_lines)
    return new_text
