import logging

from sorting.insertion_sort import insertion_sort, insertion_sort_optimized


def application_runner():
    logging.info("Start ...")
    numbers = [8, 4, 3, 1, 5, 2]
    sorted_numbers = insertion_sort_optimized(numbers)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    application_runner()
