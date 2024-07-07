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

print( merge( [1, 2, 7, 8], [3, 4, 5, 6] ) )