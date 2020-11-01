import unittest
from src.strings import *


class TestStrings(unittest.TestCase):

    def test_repeated_string(self):
        s = 'abcac'
        n = 10
        self.assertEqual(4, repeatedString(s, n))

        s = 'aba'
        n = 10
        self.assertEqual(7, repeatedString(s, n))

    def test_find_longest_common_substring(self):
        s1 = "www.educative.io/explore"
        s2 = "educative.io/edpresso"

        result = 14
        # self.assertEqual(result, longest_common_substring(s1, s2))

        S1 = "0abc321"
        S2 = "123abcdef"
        result = longest_common_substr_length(S1, S2)
        print()

    def test_shortest_substring_in_alphabet(self):
        str = 'aaccbca'
        alphabet = 'abc'
        actual = shortest_substring_in_alphabet(str, alphabet)
        self.assertEqual('bca', actual)
        self.assertIn()

    def test_longest_substring_with_no_more_than_k_characters(self):
        str = "araaci"
        k = 2
        self.assertEqual(4, longest_substring_with_no_more_than_k_characters(str, k))

    def test_find_longest_substring_without_repeats(self):
        str = "aabccbb"
        expected = 3
        self.assertEqual(expected, find_longest_substring_without_repeats(str))

    def test_backspace_compare(self):
        str1, str2="xy#z", "xzz#"
        self.assertTrue(backspace_compare(str1, str2))