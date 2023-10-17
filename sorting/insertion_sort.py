import copy
import logging
from array import array


def insertion_sort_implementation1(numbers):
    logging.info("Sorting input array %s", numbers)
    sorted_numbers = copy.copy(numbers)
    # unsorted = [8, 4, 3, 1, 5, 2]
    # i=1 unsorted = {4, 8, 3, 1, 5, 2}

    # i=2 unsorted = {4, 3, 8, 1, 5, 2}
    # i=2 unsorted = {3, 4, 8, 1, 5, 2}

    # i=3 unsorted = {3, 4, 1, 8, 5, 2}
    # i=3 unsorted = {3, 1, 4, 8, 5, 2}
    # i=3 unsorted = {1, 3, 4, 8, 5, 2}

    # i=4 unsorted = {1, 3, 4, 8, 2, 5}
    # i=4 unsorted = {1, 3, 4, 2, 8, 5}
    # i=4 unsorted = {1, 3, 2, 4, 8, 5}
    # i=4 unsorted = {1, 2, 3, 4, 8, 5}

    # i=5 unsorted = {1, 2, 3, 4, 5, 8}

    for i in range(1, len(sorted_numbers)):
        logging.info("Current element: %s", sorted_numbers[i])
        if sorted_numbers[i] < sorted_numbers[i - 1]:
            current = sorted_numbers[i]
            sorted_numbers[i] = sorted_numbers[i - 1]
            sorted_numbers[i - 1] = current
            if i > 1:
                for j in range(i - 1, 0, -1):
                    if sorted_numbers[j] < sorted_numbers[j - 1]:
                        current = sorted_numbers[j]
                        sorted_numbers[j] = sorted_numbers[j - 1]
                        sorted_numbers[j - 1] = current
            logging.info("Current sorted array %s", sorted_numbers)

    logging.info("Sorted array %s", sorted_numbers)
    return sorted_numbers
