import unittest
from src.binary_tree_node import *


class TestBinaryTree(unittest.TestCase):

    def test_min_heap(self):
        root = Node(2)
        root.left = Node(3)
        root.right = Node(4)
        root.left.left = Node(5)
        root.left.right = Node(6)
        root.right.left = Node(8)
        root.right.right = Node(10)

        self.assertTrue(is_min_heap_recur(root))

        root.right = Node(1)
        self.assertFalse(is_min_heap_recur(root))

    def test_min_heap_iter(self):
        root = Node(2)
        root.left = Node(3)
        root.right = Node(4)
        root.left.left = Node(5)
        root.left.right = Node(6)
        root.right.left = Node(8)
        root.right.right = Node(10)

        self.assertTrue(is_min_heap_iter(root))

        root.right = Node(1)
        self.assertFalse(is_min_heap_iter(root))