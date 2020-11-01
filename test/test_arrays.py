import unittest
from src.arrays import *


class TestArrays(unittest.TestCase):

    def test_longest_common(self):
        first = [2, 0, 6, 1, 5, 3, 7]
        self.assertEqual(4, findMaxLenSubSeq(first))

    def test_min_bribes(self):
        array = [2, 1, 5, 3, 4]
        self.assertEqual(3, minimumBribes(array))

    def test_maximum_sum_subarray(self):
        array = [2, 1, 5, 1, 3, 2]
        size = 3
        self.assertEqual(9, find_max_sum_subarray(size, array))

        array = [2, 3, 4, 1, 5]
        size = 2
        self.assertEqual(7, find_max_sum_subarray(size, array))

    def test_smallest_subarray_greater_than_or_equal_to_given_sum(self):
        array = [2, 1, 5, 2, 3, 2]
        sum = 7
        self.assertEqual(2, smallest_subarray_greater_than_or_equal_to_given_sum(sum, array))

    def test_fruits_into_baskets(self):
        fruit=['A', 'B', 'C', 'A', 'C']
        self.assertEqual(3, fruits_into_baskets(fruit))

    def test_pair_with_targetsum(self):
        input = [1, 2, 3, 4, 6]
        target=6
        expected = [1, 3]
        self.assertEqual(expected, pair_with_targetsum(input, target))

    def test_make_squares(self):
        arr = [-2, -1, 0, 2, 3]
        expected = [0, 1, 4, 4, 9]
        self.assertEqual(expected, make_squares(arr))

    def test_shortest_window_sort(self):
        input = [1, 2, 5, 3, 7, 10, 9, 12]
        output = 5
        self.assertEqual(output, shortest_window_sort(input))

    def test_find_missing_number(self):
        input = [4, 0, 3, 1]
        output = 2
        self.assertEqual(output, find_missing_number(input))