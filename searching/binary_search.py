import logging


def search(numbers, number):
    logging.info("Starting searching %d in array %s", number, numbers)
    # numbers = [3, 9, 12, 15, 20, 21, 24, 35, 43] len = 9
    # number = 43
    left = 0
    right = len(numbers) - 1
    is_ascending = sorted_ascending(numbers)
    while right >= left:
        i = (left + right) // 2
        if numbers[i] == number:
            return i

        if is_ascending:
            if number > numbers[i]:
                left = i + 1
                right = len(numbers) - 1
            else:
                left = 0
                right = i - 1
        else:
            if number > numbers[i]:
                left = 0
                right = i - 1
            else:
                left = i + 1
                right = len(numbers) - 1

    return -1


def sorted_ascending(numbers):
    if len(numbers) > 0:
        return bool(numbers[0] < numbers[len(numbers) - 1])
    return bool(0)
