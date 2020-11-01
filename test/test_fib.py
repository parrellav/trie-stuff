import unittest
from src.fib import *


class TestFib(unittest.TestCase):

    def test_fib_memoiz(self):
        self.assertEqual(3, fib_map(5))

