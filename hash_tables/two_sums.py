# WRITE TWO_SUM FUNCTION HERE #
#                             #
#                             #
#                             #
#                             #
###############################
def two_sum_practice(nums, target):
    hash_map = {}
    for index, number in enumerate(nums):
        if index not in hash_map:
            hash_map[index] = number
        temp = index - 1
        while temp >= 0:
            if hash_map[temp] + hash_map[index] == target:
                return [temp, index]
            temp -= 1
    return []

def two_sum(nums, target):
    num_map = {}
    for index, number in enumerate(nums):
        complement = target - number

        if complement in num_map:
            return [num_map[complement], index]
        num_map[number] = index
    return []

print(two_sum([5, 1, 7, 2, 9, 3], 10))
print(two_sum([4, 2, 11, 7, 6, 3], 9))
print(two_sum([10, 15, 5, 2, 8, 1, 7], 12))
print(two_sum([1, 3, 5, 7, 9], 10))
print(two_sum([1, 2, 3, 4, 5], 10))
print(two_sum([1, 2, 3, 4, 5], 7))
print(two_sum([1, 2, 3, 4, 5], 3))
print(two_sum([], 0))

"""
    EXPECTED OUTPUT:
    ----------------
    [1, 4]
    [1, 3]
    [0, 3]
    [1, 3]
    []
    [2, 3]
    [0, 1]
    []

"""


