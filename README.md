# Insertion Sort Optimized

"insertion_sort_optimized" is a Python implementation of the insertion sort algorithm, which sorts an unsorted list of numbers in an ascending order. 

## Usage

```python
from insertion_sort_optimized import insertion_sort_optimized

numbers = [6, 2, 8, 5, 3, 1]
sorted_numbers = insertion_sort_optimized(numbers)

print(sorted_numbers)
```

## Output

```
[1, 2, 3, 5, 6, 8]
```

## Functions

### insertion_sort_optimized(numbers: List[int]) -> List[int]

The function takes a list of integers and returns a new list containing the input values sorted in ascending order.

**Parameters**:

- `numbers` (List[int]): The input list of integers to be sorted.

**Returns**:

- A new list (List[int]) containing the input values sorted in ascending order.

**Example**:

```python
sorted_numbers = insertion_sort_optimized([64, 34, 25, 12, 22, 11, 90])
print(sorted_numbers)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

## Logging

The function logs information about each step in the sorting process. To enable/disable logging, you can configure the logging settings as per your requirements.

## Dependencies

This implementation has no external dependencies. It uses built-in Python libraries "copy" and "logging".

## Performance

The worst-case and average case time complexity of this algorithm is O(N^2), where N is the number of elements in the input list. The best-case time complexity is O(N), which occurs when the input list is already sorted.

## License

This implementation is available under the [MIT License](https://opensource.org/licenses/MIT).