# Binary Search and Insertion Sort Functions

This is a Python implementation of two common algorithms: Binary search and Insertion sort.

## Binary Search

The `search()` function takes a sorted array `numbers` and a `number` as input and returns the index of the specified number in the array, or `-1` if the number is not present.

The function first determines if the input array is sorted in ascending order and then performs the binary search as appropriate.

```python
def search(numbers, number):
    ...
```

## Insertion Sort

The `sort()` function takes an array `numbers` as input and returns a sorted copy of the array using the Insertion sort algorithm. The input array is not modified.

This insertion sort implementation is stable, meaning that the input order of equal elements is preserved in the output.

```python
def sort(numbers):
    ...
```

## Usage

To use these algorithms, simply import the functions and apply them to your data.

```python
from binary_search_and_insertion_sort import search, sort

# Example array and number to find
numbers = [3, 9, 12, 15, 20, 21, 24, 35, 43]
number = 43

# Find the index of the number using binary search
index = search(numbers, number)
print(f"The index of {number} in the array is: {index}")

# Sort the array using insertion sort
sorted_numbers = sort(numbers)
print(f"Sorted array: {sorted_numbers}")
```

## Logging

The functions include logging statements that can be useful for debugging. To enable logging, add the following code to your script:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
```

This will output logging messages from the functions to the console while running. You can adjust the logging level to suit your needs. For example, change `level=logging.DEBUG` to `level=logging.INFO` to only show information messages.