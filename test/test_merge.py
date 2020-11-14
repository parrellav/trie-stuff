import unittest
import copy
from src.merge import *


class TestQuick(unittest.TestCase):

    def test_merge(self):
        lst = [3, 2, 1, 5, 4]
        expected = copy.deepcopy(lst)
        expected.sort()
        merge_sort(lst)
        self.assertListEqual(expected, lst)

    def test_merge2(self):
        lst = [54,26,93,17,77,31,44,55,20]
        expected = copy.deepcopy(lst)
        expected.sort()
        merge_sort(lst)
        self.assertListEqual(expected, lst)
