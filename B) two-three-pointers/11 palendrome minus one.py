"""Given a non-empty string s, you may delete at most one character. 
Judge whether you can make it a palindrome."""
"""
def pal_minus_one(s):
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if s[p1] != s[p2]:
            s1 = s[:p1] + s[(p1 + 1):]#string without p1
            s2 = s[:p2] + s[(p2 + 1):]#string withtou p2
            #pallendrome equals itself reversed
            #IF either string doesnt then no solution works
            return s1 == s1[::-1] or s2 == s2[::-1]
        p1 += 1
        p2 -= 1
    return True
"""

def pal_minus_one(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            #string with char left removed -- CALL A
            str_a = ''.join([s[i] for i in range(len(s)) if i != left])
            #string with char right removed -- CALL B
            str_b = ''.join([s[i] for i in range(len(s)) if i != right])
            # check if A == reversed(A) or B == reversed(B)
            return str_a == str_a[::-1] or str_b == str_b[::-1]
        left += 1
        right -= 1
    return True

assert pal_minus_one('racecarr') == True
assert pal_minus_one('raceecar') == True
assert pal_minus_one('rabcebcar') == False
assert pal_minus_one('racecar') == True
assert pal_minus_one('tibet') == False

print('all tests have passed!')