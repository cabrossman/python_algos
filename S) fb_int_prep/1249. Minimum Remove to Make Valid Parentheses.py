"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses
 ( '(' or ')', in any positions ) so that the resulting 
 parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), 
where A and B are valid strings, or
It can be written as (A), where A is a valid string.

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Input: s = "a)b(c)d"
Output: "ab(c)d"

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
"""

def pars(string):
    str_lst = list(string)
    stack = []
    for i, s in enumerate(string):
        if s == '(':
            stack.append(i) #append indicies of list to stack
        elif s ==')':
            if stack:
                stack.pop()
            else:
                str_lst[i] = '' #blank it
    while stack: #if extra in stack blank indicies
        idx = stack.pop()
        str_lst[idx] = ''

    return ''.join(str_lst)

assert pars('lee(t(c)o)de)') == 'lee(t(c)o)de'
assert pars('a)b(c)d') == 'ab(c)d'
assert pars('))((') == ''
print('all tests passed!')