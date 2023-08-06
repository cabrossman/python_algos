"""
Given a string, find all of its permutations preserving the character sequence but changing case.

Input: "ad52"
Output: ["ad52", "Ad52", "aD52", "AD52"]

Input: "ab7c"
Output: ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]

BFS
complexity = O(N*2^N)
"""

from collections import deque

def find_letter_case_string_permutations(s):
    permutations = [s]
    for i in range(len(s)):
        if s[i].isnumeric():
            continue
        for j in range(len(permutations)):
            perm = list(permutations[j])
            perm[i] = perm[i].swapcase()
            permutations.append(''.join(perm))
    return permutations


assert find_letter_case_string_permutations("ad52") == [
    "ad52", "Ad52", "aD52", "AD52"
]
assert find_letter_case_string_permutations("ab7c") == [
    "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
]

print("all tests have passed!")