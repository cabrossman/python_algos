"""
Given a string, s, that represents a DNA subsequence, and a number k, 
return all the contiguous subsequences (substrings) of length k
that occur more than once in the string. 

The order of the returned subsequences does not matter. 
If no repeated substring is found, the function should return an empty set.
"""

def subseq(s,k):
    start = 0
    input_set = set()
    output_set = set()
    for end in range(k, len(s), 1):
        if s[start:end] in input_set:
            output_set.add(s[start:end])
        else:
            input_set.add(s[start:end])
        start += 1
    formatting_output = list(output_set)
    formatting_output.sort()
    return formatting_output

assert subseq("AAAAACCCCCAAAAACCCCCC" , 8) == ["AAAAACCC", "AAAACCCC", "AAACCCCC"]
assert subseq("GGGGGGGGGGGGGGGGGGGGGGGGG" , 12) == ["GGGGGGGGGGGG"]
outlst = ["CCCCCCCTTT", "CCCCCCTTTT", "CCCCCTTTTT", "CCCCTTTTTT", "TCCCCCCCTT", 
          "TTCCCCCCCT", "TTTCCCCCCC", "TTTTCCCCCC", "TTTTTCCCCC"]
assert subseq("TTTTTCCCCCCCTTTTTTCCCCCCCTTTTTTT" , 10) == outlst
print('all tests have passed!')
