import unittest
from src.merge import *


class TestQuick(unittest.TestCase):

    def test_merge(self):
        lst = [3, 2, 1, 5, 4]
        merge_sort(lst)

        print("Sorted list is: ", lst)
