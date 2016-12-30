'''
Merge sort

Implementation of Merge sort with a time complexity O(n log n)

Oliver Edholm, 14 years old 2016-12-21 22:39
'''
# imports
from random import randint
from six.moves import xrange
from math import floor


# functions
def rand_list(n_elements, min_num, max_num):
    return [randint(min_num, max_num) for _ in xrange(n_elements)]


def merge(lst, start_index, mid_index, end_index):
    sub_lst1_len = mid_index - start_index + 1
    sub_lst2_len = end_index - mid_index
    
    sub_lst1 = []
    sub_lst2 = []
    for i, j in zip(range(sub_lst1_len), range(sub_lst2_len)):
        sub_lst1.append(lst[i + start_index])
        sub_lst2.append(lst[j + mid_index + 1])
    
    if len(sub_lst1) != sub_lst1_len:
        sub_lst1.append(lst[sub_lst1_len - 1 + start_index])

    k = start_index
    i = 0
    j = 0
    while i < sub_lst1_len and j < sub_lst2_len:
        if sub_lst1[i] < sub_lst2[j]:
            lst[k] = sub_lst1[i]
            i += 1
        else:
            lst[k] = sub_lst2[j]
            j += 1

        k += 1

    while i < sub_lst1_len:
        lst[k] = sub_lst1[i]
        i += 1
        k += 1

    while j < sub_lst2_len:
        lst[k] = sub_lst2[j]
        j += 1
        k += 1


def merge_sort(lst, start_index, end_index):  # recursive
    if start_index < end_index:
        mid_index = floor((start_index + end_index) / 2)
        
        merge_sort(lst, start_index, mid_index)
        merge_sort(lst, mid_index + 1, end_index)
        merge(lst, start_index, mid_index, end_index)


def main():
    lst = rand_list(20, 1, 1000)

    print('initial list: {}'.format(lst))
    
    merge_sort(lst, 0, len(lst) - 1)
    print('sorted list: {}'.format(lst))

if __name__ == '__main__':
    main()

