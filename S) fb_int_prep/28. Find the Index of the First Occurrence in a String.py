"""
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

"""
from collections import deque
def find(haystack, needle):
    window_len = len(needle)
    substr = deque()
    for i in range(len(haystack)):
        if i < window_len:
            substr.append(haystack[i])
            continue
        if ''.join(substr) == needle:
            return i - window_len
        else:
            substr.popleft()
            substr.append(haystack[i])
    return -1

def strStr(haystack, needle): ###alt
    if needle == '':
        return 0
    needle_length = len(needle)
    for i in range(len(haystack) - needle_length + 1):
        if haystack[i:i+needle_length] == needle:
            return i
    return -1

assert find(haystack = "sadbutsad", needle = "sad") == 0
assert find(haystack = "leetcode", needle = "leeto") == -1
print('all tests passed!')
        