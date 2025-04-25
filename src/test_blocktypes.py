import unittest

from blocktypes import block_to_block_type, BlockType

class TestBlockToBlock(unittest.TestCase):
    def test_heading(self):
        block = "# Heading"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type, BlockType.HEADING
    )

    def test_code(self):
        block = "```this is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type, BlockType.CODE
        )

    def test_quote(self):
        block = """>These are quotes\n>So interesting\n>Turd"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type, BlockType.QUOTE
        )
        
    def test_unordered_list(self):
        block = """- These are unordered lines\n- So interesting\n- Turd"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type, BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        block = """1. These are ordered lines\n2. So interesting\n3. turd"""
        block_type = block_to_block_type(block)
        self.assertEqual(
            block_type, BlockType.ORDERED_LIST
        )
    

