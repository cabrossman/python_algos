"""
Matching Pairs
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.
Signature
int matchingPairs(String s, String t)
Input
s and t are strings of length N
N is between 2 and 1,000,000
Output
Return an integer denoting the maximum number of matching pairs
Example 1
s = "abcd"
t = "adcb"
output = 4
Explanation:
Using 0-based indexing, and with i = 1 and j = 3, s[1] and s[3] can be swapped, making it  "adcb".
Therefore, the number of matching pairs of s and t will be 4.
Example 2
s = "mno"
t = "mno"
output = 1
Explanation:
Two indices have to be swapped, regardless of which two it is, only one letter will remain the same. If i = 0 and j=1, s[0] and s[1] are swapped, making s = "nmo", which shares only "o" with t.

"""



def matching_pairs(s, t):
  if s == '':
    return 0
  if s == t:
    return max(0,len(s) - 2)
  
  matches = 0
  swap_flag = 0
  i = 0
  while i < len(s):
    if s[i] == t[i]:
      matches += 1
      i += 1
    elif swap_flag <1:
      j = i
      while j < len(s) and s[i] != t[j]:
        j += 1
      t_list = list(t)
      t_list[i], t_list[j] = t[j], t[i]
      t = ''.join(t_list)
      swap_flag = 1
  return matches

s_1, t_1 = "abcde", "adcbe"
expected_1 = 5
output_1 = matching_pairs(s_1, t_1)

assert output_1 == expected_1

s_2, t_2 = "abcd", "abcd"
expected_2 = 2
output_2 = matching_pairs(s_2, t_2)

assert output_2 == expected_2