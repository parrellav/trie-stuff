import unittest
from src.quick import *



class TestQuick(unittest.TestCase):

    def test_quick(self):
        lst = [5, 4, 2, 1, 3]
        actual = quick_sort(lst, 0, len(lst) - 1)

        # Printing Sorted list
        self.assertListEqual(sorted(lst), actual)
        print("Sorted list: ", lst)

    # def test_merge(self):
    #     lst = [3, 2, 1, 5, 4]
    #     merge_sort(lst)
    #
    #     print("Sorted list is: ", lst)
