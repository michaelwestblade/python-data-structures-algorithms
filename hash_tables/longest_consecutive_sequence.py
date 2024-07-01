# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################

def longest_consecutive_sequence(number_list):
    number_set = set(number_list)
    longest_sequence = 0

    for number in number_list:
        if number - 1 not in number_set:
            current_number = number
            current_sequence = 1

            while current_number + 1 in number_set:
                current_number += 1
                current_sequence += 1

            longest_sequence = max(current_sequence, longest_sequence)
    return longest_sequence

print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""