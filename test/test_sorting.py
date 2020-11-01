import unittest
from src.sorting import *
from src.quick import *
from src.quickVinny import quick_sort as vinny_quick


class TestArrays(unittest.TestCase):

    def test_sorting(self):
        expected = [2, 2, 3, 3, 4, 4, 5, 6, 8]
        given = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(expected, quick_sort(given, 0, len(given)-1))

    def test_vinny_sorting(self):
        expected = [2, 2, 3, 3, 4, 4, 5, 6, 8]
        given = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(expected, vinny_quick(given, 0, len(given)-1))

    def test_activity_notifications(self):
        expenditures = [2, 3, 4, 2, 3, 6, 8, 4, 5]
        self.assertEqual(2, activityNotifications(expenditures, 5))

