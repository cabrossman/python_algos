"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".

 O(N)
"""

def main(s,k):
  window_start, largest_sub_array = 0, 0
  for window_end in range(len(s)):
    substr = s[window_start:window_end]
    while len(set(substr)) == k and window_start < window_end:
      largest_sub_array = max(largest_sub_array, window_end - window_start + 1)
      window_start = window_start + 1
      substr = s[window_start:window_end]
  return largest_sub_array if largest_sub_array != 0 else len(s)


assert main('araaci',2) == 4
assert main('araaci', 1) == 2
assert main('cbbebi', 3) == 5
assert main('cbbebi', 10) == 6

print('all tests past!')


