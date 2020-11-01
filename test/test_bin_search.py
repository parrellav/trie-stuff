import unittest
from src.binary_search import *


class TestArrays(unittest.TestCase):

    def test_binary_search(self):
        lst = [0, 1, 2, 4, 5, 7, 9]
        self.assertTrue(find_value_in_sorted_list(lst, 2))
        self.assertFalse(find_value_in_sorted_list(lst, 14))
