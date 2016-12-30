'''
Binary search

Implementation of the algorithm Binary search with a time complexity of
O(log2 n).

Oliver Edholm, 14 years old 2016-12-21 16:45
'''
# imports
from random import randint
from six.moves import xrange
from math import floor


# functions
def rand_list(n_elements, min_num, max_num):
    return [randint(min_num, max_num) for _ in xrange(n_elements)]


def binary_search(lst, to_find, start_index, end_index):  # recursive
    mid_index = floor((start_index + end_index) / 2)

    item = lst[mid_index]
    if item < to_find:
        return binary_search(lst, to_find, mid_index, end_index)
    elif item > to_find:
        return binary_search(lst, to_find, start_index, mid_index)
    else:
        return mid_index


def main():
    lst = rand_list(20, 1, 1000)
    lst = list(set(lst))  # no duplicates, for easier checking
    lst.sort()

    item_to_find = lst[randint(0, len(lst) - 1)]
    print('finding index of {} in {}'.format(item_to_find, lst))

    item_index = binary_search(lst, item_to_find, 0, len(lst) - 1)

    print('index of {} is {}'.format(item_to_find, item_index))


if __name__ == '__main__':
    main()

