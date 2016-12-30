'''
Quick select

Implementation of Quick select with a time complexity of O(n).

Oliver Edholm, 14 years old 2016-12-22 16:38
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
    swap(lst, i, end_index)

    return i


def quick_select(lst, k, start_index, end_index):  # recursive
    pivot_index = partition(lst, start_index, end_index)

    if pivot_index < k - 1:
        return quick_select(lst, k, pivot_index + 1, end_index)    
    elif pivot_index > k - 1:
        return quick_select(lst, k, start_index, pivot_index - 1)
    else:
        return lst[pivot_index]


def main():
    lst = rand_list(20, 1, 1000)

    print('list to quick select: {}'.format(lst))

    k = randint(1, len(lst) - 1)

    lst_copy = lst[:]
    index = quick_select(lst_copy, k, 0, len(lst) - 1)
    print('the index of the item in a sorted version of the \
list at pos {} is {}'.format(k, index))
   

if __name__ == '__main__':
    main()

