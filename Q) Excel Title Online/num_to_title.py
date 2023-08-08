"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Input: columnNumber = 1
Output: "A"

Input: columnNumber = 28
Output: "AB"

Input: columnNumber = 701
Output: "ZY"

Constraaints
1 <= columnNumber <= 2^31 - 1
"""
from collections import deque
def convertToTitle(n):
    s = deque()
    while n > 0:
        n -= 1
        rem = n % 26
        letter_idx = ord('A') + rem
        letter_chr = chr(letter_idx)
        s.appendleft(letter_chr)
        n = n // 26
    return ''.join(s)


assert convertToTitle(1) == 'A'
assert convertToTitle(28) == 'AB'
assert convertToTitle(701) == 'ZY'
print('all tests have passed!')


