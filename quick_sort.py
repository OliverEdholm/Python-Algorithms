'''
Quick sort

Implementation of Quick sort with a time complexity of O(n log n).

Oliver Edholm, 14 years old 2016-12-22 14:14
'''
# imports
from random import randint
from six.moves import xrange


# functions
def rand_list(n_elements, min_num, max_num):
    return [randint(min_num, max_num) for _ in xrange(n_elements)]


def swap(lst, index1, index2):
    temp = lst[index1]
    lst[index1] = lst[index2]
    lst[index2] = temp


def partition(lst, start_index, end_index):
    pivot = lst[end_index]

    i = start_index - 1
    for j in range(start_index, end_index):
        if lst[j] < pivot:
            i += 1
            swap(lst, i, j)

    i += 1
    swap(lst, end_index, i)

    return i


def quick_sort(lst, start_index, end_index):  # recursive
    if start_index < end_index:
        pivot_index = partition(lst, start_index, end_index)

        quick_sort(lst, start_index, pivot_index - 1)
        quick_sort(lst, pivot_index + 1, end_index)


def main():
    lst = rand_list(20, 1, 1000)

    print('initial list: {}'.format(lst))

    quick_sort(lst, 0, len(lst) - 1)
    print('sorted list: {}'.format(lst))


if __name__ == '__main__':
    main()

