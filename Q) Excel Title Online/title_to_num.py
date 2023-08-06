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

Input: A
Output: 1

Input: "AB"
Output: columnNumber = 28

Input: "ZY"
Output: 701

Constraaints
valid char
"""

def convertToInt(COLS):
    tot = 0 #running total
    for i, col in enumerate(COLS[::-1]): # reverse list so we pop each letter off in reverse
        char_int = ord(col) - ord('A') + 1 #distance from A - indexed at 1
        subtotal = char_int*(26**i) #convert from base 26 to base 10
        tot = tot + subtotal # add to running total
    return tot

assert convertToInt('A') == 1
assert convertToInt('AB') == 28
assert convertToInt('ZY') == 701
print('all tests have passed!')


