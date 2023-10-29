import logging

from sorting.insertion_sort import sort


def application_runner():
    logging.info("Start main...")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    application_runner()
