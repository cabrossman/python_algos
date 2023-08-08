"""
Given a string, s, that represents a DNA subsequence, and a number k, 
return all the contiguous subsequences (substrings) of length k
that occur more than once in the string. 

The order of the returned subsequences does not matter. 
If no repeated substring is found, the function should return an empty set.
"""

def subseq(s,k):
    input_set, output_set = set(), set()
    for end in range(k, len(s)):
        substr = s[end - k :end]
        if substr in input_set:
            output_set.add(substr)
        else:
            input_set.add(substr)
    return output_set


assert subseq("AAAAACCCCCAAAAACCCCCC" , 8) == {"AAAAACCC", "AAAACCCC", "AAACCCCC"}
assert subseq("GGGGGGGGGGGGGGGGGGGGGGGGG" , 12) == {"GGGGGGGGGGGG"}
outlst = {"CCCCCCCTTT", "CCCCCCTTTT", "CCCCCTTTTT", "CCCCTTTTTT", "TCCCCCCCTT", 
          "TTCCCCCCCT", "TTTCCCCCCC", "TTTTCCCCCC", "TTTTTCCCCC"}
assert subseq("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT" , 10) == outlst
print('all tests have passed!')
