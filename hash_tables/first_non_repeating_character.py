# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(string: str) -> str:
    char_dict = {}
    for char in string:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    for char in string:
        if char_dict[char] == 1:
            return char


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""