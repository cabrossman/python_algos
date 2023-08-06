"""
Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

def vpal_m1(s):
    p1,p2 = 0, len(s) -1
    while p1 < p2:
        if s[p1] == s[p2]:
            p1 += 1
            p2 -= 1
        else:
            #make two string copies one for p1 and one for p2
            #remove the single problem character from each copy p1, p2
            # check if string equals itself backwards
            #if atleast one does return true
            s1, s2 = list(s), list(s)
            s1[p1], s2[p2] = '', ''
            s1, s2 = ''.join(s1), ''.join(s2)
            return s1 == s1[::-1] or s2 == s2[::-1]
    return True

assert vpal_m1('xyay^x') == True
assert vpal_m1('x^yayx') == True
assert vpal_m1('aba') == True
assert vpal_m1('abca') == True
assert vpal_m1('abc') == False
assert vpal_m1('raceecar') == True
print('all tests passed')