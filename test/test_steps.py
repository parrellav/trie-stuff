import unittest
from src.stair import *


class TestSteps(unittest.TestCase):

    def test_count_steps_recurse(self):
        steps = 4
        self.assertEqual(7, count_ways_recurse(steps))

    def test_count_steps_memoiz(self):
        steps = 4
        self.assertEqual(7, count_steps_memoiz(steps))