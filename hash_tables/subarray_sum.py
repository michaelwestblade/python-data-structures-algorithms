# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def subarray_sum_practice(number_list, target):
    number_map = {}
    for index, number in enumerate(number_list):
        if index not in number_map:
            number_map[index] = number
        else:
            number_map[index] += number

        if number_map[index] == target:
            return [index, index]

        temp = index - 1
        while temp >= 0:
            number_map[temp] += number
            if number_map[temp] == target:
                return [temp, index]
            temp -= 1

    return []

def subarray_sum(number_list, target):
    sum_index = {0: -1}
    current_sum = 0
    for index, number in enumerate(number_list):
        current_sum += number
        if current_sum - target in sum_index:
            return [sum_index[current_sum- target] + 1, index]
        sum_index[current_sum] = index
    return []


nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
