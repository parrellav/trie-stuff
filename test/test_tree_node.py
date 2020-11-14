import unittest
from src.tree_node import *


class TestTreeNode(unittest.TestCase):

    def test_has_path(self):
        root = TreeNode(12)
        root.left = TreeNode(7)
        root.right = TreeNode(1)
        root.left.left = TreeNode(9)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(5)
        self.assertTrue(has_path(root, 23))
        self.assertFalse(has_path(root, 16))
