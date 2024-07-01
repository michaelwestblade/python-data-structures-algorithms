# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def find_pairs(num_list_1, num_list_2, target):
    set1 = set(num_list_1)
    pairs = []

    for number in num_list_2:
        complement = target - number
        if complement in set1:
            pairs.append((complement,number))
    return pairs



arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""