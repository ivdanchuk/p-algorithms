import unittest

from searching.binary_search import search


class TestBinarySort(unittest.TestCase):
    def test_should_find_last_in_asc_array(self):
        numbers = [3, 9, 12, 15, 20, 21, 24, 35, 43]
        number = 43
        self.assertEqual(search(numbers, number), 8)

    def test_should_find_first_in_asc_array(self):
        numbers = [3, 9, 12, 15, 20, 21, 24, 35, 43]
        number = 3
        self.assertEqual(search(numbers, number), 0)

    def test_should_find_last_in_des_array(self):
        numbers = [45, 30, 19, 17, 16, 15, 13, 12, 11]
        number = 11
        self.assertEqual(search(numbers, number), 8)

    def test_should_find_first_in_des_array(self):
        numbers = [3, 9, 12, 15, 20, 21, 24, 35, 43]
        number = 3
        self.assertEqual(search(numbers, number), 0)

    def test_should_handle_empty_array(self):
        numbers = []
        number = 43
        self.assertEqual(search(numbers, number), -1)

    def test_should_handle_short_array(self):
        numbers = [43]
        number = 43
        self.assertEqual(search(numbers, number), 0)
