from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    heading_regex = r"^#{1,6}\s+.*"
    code_regex = r"^```(?:[^`\n]*```$|[\s\S]*?^```)"
    quote_regex = r"^>(?:.*(?:\n>.*)*)$"
    unordered_list_regex = r"^(?:-\s+.*(?:\n-\s+.*)*)$"
    ordered_list_regex = r"^(?:\d+\.\s+.*(?:\n\d+\.\s+.*)*)$"
    if re.match(heading_regex, block):
        return BlockType.HEADING
    elif re.match(code_regex, block):
        return BlockType.CODE
    elif re.match(quote_regex, block):
        return BlockType.QUOTE
    elif re.match(unordered_list_regex, block):
        return BlockType.UNORDERED_LIST
    elif re.match(ordered_list_regex, block):
        lines = block.split("\n")
        for i in range(1,len(lines)):
            if lines[i-1].startswith(f"{i}"):
                continue
            else:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    




