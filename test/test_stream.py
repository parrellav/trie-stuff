import unittest
from src.stream import *


class TestStream(unittest.TestCase):

    def test_find_mediam(self):
        medianOfAStream = MedianOfAStream()
        medianOfAStream.insert_num(3)
        medianOfAStream.insert_num(1)
        self.assertEqual(2, medianOfAStream.find_median())

