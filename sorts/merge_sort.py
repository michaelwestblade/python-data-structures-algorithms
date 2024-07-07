from typing import List

def merge(list1: List, list2: List) -> List:
    combined = []
    list1_index = 0
    list2_index = 0

    while list1_index < len(list1) and list2_index < len(list2):
        if list1[list1_index] < list2[list2_index]:
            combined.append(list1[list1_index])
            list1_index += 1
        else:
            combined.append(list2[list2_index])
            list2_index += 1

    while list1_index < len(list1):
        combined.append(list1[list1_index])
        list1_index += 1

    while list2_index < len(list2):
        combined.append(list2[list2_index])
        list2_index += 1

    return combined

def merge_sort(list_to_sort: List) -> List:
    # if we have only one item, return (BASE CASE)
    if len(list_to_sort) <= 1:
        return list_to_sort
    mid_index = len(list_to_sort) // 2
    # create list from 0 up to but not including mid_index
    # and call merge_sort recursively
    left = merge_sort(list_to_sort[:mid_index])
    # create list from mid_index to the end
    # and call merge_sort recursively
    right = merge_sort(list_to_sort[mid_index:])

    return merge(left, right)

print( merge( [1, 2, 7, 8], [3, 4, 5, 6] ) )

print(merge_sort([ 4, 2, 6, 5, 1, 3 ]))