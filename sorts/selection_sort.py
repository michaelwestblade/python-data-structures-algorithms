from typing import List


def selection_sort(list_to_sort: List[int]) -> List[int]:
    """
    apply selection sort to a list
    :param list_to_sort:
    :return:
    """
    for outer_index in range(len(list_to_sort) - 1):
        min_index = outer_index
        # for each index look ahead for the smallest value and swap
        for inner_index in range(outer_index + 1, len(list_to_sort)):
            if list_to_sort[inner_index] < list_to_sort[min_index]:
                min_index = inner_index

        if min_index != outer_index:
            # swap the item at min index with the item at outer_index
            temp = list_to_sort[outer_index]
            list_to_sort[outer_index] = list_to_sort[min_index]
            list_to_sort[min_index] = temp

    return list_to_sort

print(selection_sort([ 4, 2, 6, 5, 1, 3 ]))
