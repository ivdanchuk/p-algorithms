import unittest

from sorting.insertion_sort import sort


class TestInsertingSort(unittest.TestCase):
    def test_should_sort_array(self):
        unsorted_input = [8, 4, 3, 1, 5, 2]
        sorted_input = sort(unsorted_input)
        self.assertEqual(sorted_input, [1, 2, 3, 4, 5, 8])

    def test_should_sort_array_of_one(self):
        unsorted_input = [8]
        sorted_input = sort(unsorted_input)
        self.assertEqual(sorted_input, [8])

    def test_should_sort_array_of_two(self):
        unsorted_input = [8, 4]
        sorted_input = sort(unsorted_input)
        self.assertEqual(sorted_input, [4, 8])

    def test_should_sort_empty(self):
        unsorted_input = []
        sorted_input = sort(unsorted_input)
        self.assertEqual(sorted_input, [])


if __name__ == '__main__':
    unittest.main()
