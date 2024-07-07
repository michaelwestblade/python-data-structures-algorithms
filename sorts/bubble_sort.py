from typing import List


def bubble_sort(list_to_sort: List[int]) -> List[int]:
    """
    bubble sort a list
    :param list_to_sort:
    :return:
    """
    for reverse_index in range(len(list_to_sort) - 1, 0, -1):
        for forward_index in range(reverse_index):
            if list_to_sort[forward_index] > list_to_sort[forward_index + 1]:
                temp = list_to_sort[forward_index]
                list_to_sort[forward_index] = list_to_sort[forward_index + 1]
                list_to_sort[forward_index + 1] = temp

    return list_to_sort

print(bubble_sort([ 4, 2, 6, 5, 1, 3 ]))
