import unittest
from src.knapsack import *


class TestKnapsack(unittest.TestCase):

    def test_0_1_knapsack(self):
        profit = [60, 100, 120]
        profits_length = 3
        weight = [10, 20, 30]
        capacity = 50 # knapsack weight

        self.assertEqual(220, knap_sack(profit, profits_length, weight, capacity))
