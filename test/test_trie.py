import unittest
from src.trie import *
from src.trie2 import *

class TestTrie(unittest.TestCase):

    # def setUp(self):

    # def tearDown(self):

    def test_longest_common(self):
        keys = [
            "code", "coder", "coding", "codable", "codec", "codecs", "coded",
            "codeless", "codependence", "codependency", "codependent",
            "codependents", "codes", "codesign", "codesigned", "codeveloped",
            "codeveloper", "codex", "codify", "codiscovered", "codrive", "codability"
        ]
        # keys = [
        #     "code", "coder", "bob"
        # ]
        trie = Trie()
        for key in keys:
            insert(trie, key)
        self.assertEqual('cod', findLongestCommonSequence(trie))

    def test_lexographic_sort(self):
        # given set of keys
        my_list = [
            "lexicographic", "sorting", "of", "a", "set", "of", "keys", "can", "be",
            "accomplished", "with", "a", "simple", "trie", "based", "algorithm",
            "we", "insert", "all", "keys", "in", "a", "trie", "output", "all",
            "keys", "in", "the", "trie", "by", "means", "of", "preorder",
            "traversal", "which", "results", "in", "output", "that", "is", "in",
            "lexicographically", "increasing", "order", "preorder", "traversal",
            "is", "a", "kind", "of", "depth", "first", "traversal"
        ]
        # dict = ["bat", "bad"]
        head = Trie2()

        # insert all keys of dictionary into trie
        for word in my_list:
            insert_ord(head, word)
        sort_lex(head, '')