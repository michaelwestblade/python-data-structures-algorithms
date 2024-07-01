# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
from typing import List


def remove_duplicates(number_list: List[int]) -> List[int]:
    number_set = set(number_list)
    return list(number_set)


my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 3, 4, 8, 9, 5]
new_list = remove_duplicates(my_list)
print(new_list)



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

    (Order may be different as sets are unordered)

"""