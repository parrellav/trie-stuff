import unittest
from src.dutch_national import *


class TestArrays(unittest.TestCase):

    def test_sort_list_of_zeros_ones_twos(self):
        lst = [2, 0, 0, 1, 2, 1, 0]
        expected = [0, 0, 0, 1, 1, 2, 2]
        self.assertEqual(expected, sort_list_of_zero_one_two(lst))
