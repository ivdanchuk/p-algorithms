import logging
import unittest

from sorting.insertion_sort import insertion_sort_implementation1


class TestInsertingSort(unittest.TestCase):

    def test_should_sort1(self):
        unsorted_input = [8, 4, 3, 1, 5, 2]
        sorted_input = insertion_sort_implementation1(unsorted_input)
        self.assertEqual(sorted_input, [1, 2, 3, 4, 5, 8])

    def test_should_sort2(self):
        unsorted_input = [8, 4]
        sorted_input = insertion_sort_implementation1(unsorted_input)
        self.assertEqual(sorted_input, [4, 8])

    def test_should_sort3(self):
        unsorted_input = [8]
        sorted_input = insertion_sort_implementation1(unsorted_input)
        self.assertEqual(sorted_input, [8])

    def test_should_sort4(self):
        unsorted_input = []
        sorted_input = insertion_sort_implementation1(unsorted_input)
        self.assertEqual(sorted_input, [])

if __name__ == '__main__':
    unittest.main()
