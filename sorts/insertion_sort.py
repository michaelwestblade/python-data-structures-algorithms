from typing import List


def insertion_sort(list_to_sort: List[int]) -> List[int]:
    """
    apply insertion sort to a list
    :param list_to_sort:
    :return:
    """
    # iterate through list starting at index 1
    for index in range(1, len(list_to_sort)):
        temp = list_to_sort[index]
        reverse_index = index - 1

        # while temp is less than element at reverse index
        while temp < list_to_sort[reverse_index] and reverse_index >= 0:
            # swap elements
            list_to_sort[reverse_index + 1] = list_to_sort[reverse_index]
            list_to_sort[reverse_index] = temp
            # decrement reverse index
            reverse_index -= 1

    return list_to_sort

print(insertion_sort([ 4, 2, 6, 5, 1, 3 ]))