import copy
import logging


def sort(numbers):
    logging.info("Start sorting array: %s", numbers)
    sorted_numbers = copy.copy(numbers)
    for i in range(1, len(sorted_numbers)):
        current = sorted_numbers[i]
        j = i - 1

        if current < sorted_numbers[j]:
            while (j >= 0) and (sorted_numbers[j] > current):
                sorted_numbers[j + 1] = sorted_numbers[j]
                j = j - 1
            sorted_numbers[j + 1] = current
            logging.debug("Sorted array %s", sorted_numbers)

    return sorted_numbers
