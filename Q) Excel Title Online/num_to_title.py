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

def convertToTitle(idx):
    column_string = ''
    while idx > 0:
        idx -= 1
        column_string = chr((idx % 26) + ord('A')) + column_string
        idx //= 26
    return column_string


assert convertToTitle(1) == 'A'
assert convertToTitle(28) == 'AB'
assert convertToTitle(701) == 'ZY'
print('all tests have passed!')


