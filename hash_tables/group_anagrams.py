# WRITE GROUP_ANAGRAMS FUNCTION HERE #
#                                    #
#                                    #
#                                    #
#                                    #
######################################
from typing import List


def group_anagrams_practice(word_list: List[str]) -> List[List[str]]:
    hash_map = {}
    for word in word_list:
        hash_key = 0
        for char in word:
            hash_key += ord(char)
        if hash_key not in hash_map:
            hash_map[hash_key] = [word]
        else:
            hash_map[hash_key].append(word)

    return [value for value in hash_map.values()]

def group_anagrams(word_list: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for word in word_list:
        canonical = ''.join(sorted(word))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(word)
        else:
            anagram_groups[canonical] = [word]
    return list(anagram_groups.values())


print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )



"""
    EXPECTED OUTPUT:
    ----------------
    1st set:
    [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    2nd set:
    [['abc', 'cba', 'bac'], ['foo'], ['bar']]

    3rd set:
    [['listen', 'silent'], ['triangle', 'integral'], ['garden', 'ranged']]

"""