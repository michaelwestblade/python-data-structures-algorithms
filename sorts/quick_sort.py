def swap(target_list: list, index1: int, index2: int) -> None:
    """
    given a list and two indices, swap the values
    :param target_list:
    :param index1:
    :param index2:
    :return:
    """
    temp = target_list[index1]
    target_list[index1] = target_list[index2]
    target_list[index2] = temp

def pivot(list_to_check: list, pivot_index: int, end_index: int) -> int:
    # set swap index to pivot
    swap_index = pivot_index

    for loop_index in range(pivot_index + 1, end_index + 1):
        # if we find a value less than the pivot
        if list_to_check[loop_index] < list_to_check[pivot_index]:
            # increment swap index and swap values
            swap_index += 1
            swap(list_to_check, swap_index, loop_index)

    # swap pivot to where swap index is
    swap(list_to_check, pivot_index, swap_index)

    return swap_index

def quick_sort_helper(list_to_sort: list, left: int, right: int) -> list:
    if left < right:
        pivot_index = pivot(list_to_sort, left, right)
        quick_sort_helper(list_to_sort, left, pivot_index - 1)
        quick_sort_helper(list_to_sort, pivot_index + 1, right)

    return list_to_sort

def quick_sort(list_to_sort: list) -> list:
    return quick_sort_helper(list_to_sort, 0, len(list_to_sort) - 1)


list_to_sort = [4, 6, 1, 7, 3, 2, 5]
print(pivot(list_to_sort, 0, 6))
print(list_to_sort)

print(quick_sort(list_to_sort))
