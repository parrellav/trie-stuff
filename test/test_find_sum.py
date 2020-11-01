import unittest
from src.lists import *


class TestFindSum(unittest.TestCase):

    def test_find_sum(self):
        lst = [1, 21, 3, 14, 5, 60, 7, 6]
        n = 81
        self.assertEqual([21, 60], find_sum(lst, n))

    def test_pivoted_binary_search(self):
        lst = [7, 8, 9, 0, 3, 5, 6]
        n = len(lst)
        key = 3
        self.assertEqual(4, pivoted_binary_search(lst, n, key))

    def test_sort_binary_list(self):
        lst = [1, 0, 1, 0, 1, 1, 0, 0]
        expected = [0, 0, 0, 0, 1, 1, 1, 1]
        actual = sort_binary_list(lst)
        self.assertEqual(expected, actual)

    def test_find_max_prod(self):
        lst = [1, 3, 5, 2, 6]
        actual1, actual2 = find_max_prod(lst)
        expected1, expected2 = 5, 6

    def test_search_2d_list(self):
        two_d_list  =[[10, 11, 12, 13],
                   [14, 15, 16, 17],
                   [27, 29, 30, 31],
                   [32, 33, 39, 50]]

        number = 30

        self.assertTrue(search_two_d_list(two_d_list, number))

    def test_search_insert_position(self):
        lst = [1, 3, 5, 6]
        value = 5
        self.assertEqual(search_insert_position(lst, value), 2)