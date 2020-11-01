import unittest
from src.parens import *


class TestArrays(unittest.TestCase):

    def test_bal_parens_1(self):
        n = 2
        expected = ['()']
        self.assertEqual(expected, print_all_braces(n))

    def test_balanced_parens(self):
        n = 3
        expected = ['((()))', '(()())', '(())()', '()()()']
        self.assertEqual(expected, print_all_braces(n))

