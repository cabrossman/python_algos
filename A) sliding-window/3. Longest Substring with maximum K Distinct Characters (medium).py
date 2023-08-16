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

def main(s, k):
    start, max_length, char_freq = 0, 0, {}
    for end in range(len(s)):
        end_char = s[end]
        char_freq[end_char] = char_freq.get(end_char,0) + 1
        while len(char_freq) > k: #distinct characters exceeds K!
            start_char = s[start]
            char_freq[start_char] -= 1
            if char_freq[start_char] == 0:
                del char_freq[start_char]
            start += 1  # shrink the window
        max_length = max(max_length, end - start + 1)
    return max_length

assert main('araaci',2) == 4
assert main('araaci', 1) == 2
assert main('cbbebi', 3) == 5
assert main('cbbebi', 10) == 6

print('all tests past!')


