"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).


Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

def pow(x, n):
    if n < 0: #adjust for recip
        x = 1 / x
        n = -n
    result = 1
    while n:
        if n % 2 == 1:  # if store copy of BASE (equiv to X^1) dec X
            result = result * x
            n -= 1
        else:  # if n is even -> 2^4 == (2*2)^2
            x = (x * x)
            n = n/2
    return result

assert round(pow(x = 2.0, n = 10),3) == 1024.000
assert round(pow(x = 2.1, n = 3),3) == 9.261
assert round(pow(x = 2.0, n = -2),3) == 0.250
print('all tests passed')