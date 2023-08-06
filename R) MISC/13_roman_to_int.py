"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. 
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""
def roman_to_int(roman):
    out = 0
    mapp = {
        'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M': 1000,
        'IV': 4, 'IX': 9, 'XL': 40, 'XC':90, 'CD': 400, 'CM': 900
    }
    for i in range(len(roman)):
        char1 = roman[i]
        if i == 0:
            out += mapp[char1]
            continue
        char2 = roman[i-1]
        if (char2 + char1) in mapp:
            out -= mapp[char2]
            out += mapp[char2 + char1]
        else:
            out += mapp[char1]
    return out

assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994
print('all tests have passed!')