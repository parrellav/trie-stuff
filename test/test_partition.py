import unittest
from src.partition import *


class TestArrays(unittest.TestCase):

    def test_longest_common(self):
        input = {1, 2, 3, 4}
        self.assertTrue(can_partition(input))
