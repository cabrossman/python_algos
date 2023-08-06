
def remove_duplicates(string):
    stack = []
    for s in string:
        if stack and s == stack[-1]:
            stack.pop()
        else:
            stack.append(s)
    return ''.join(stack)

assert remove_duplicates('g') == 'g'
assert remove_duplicates("ggaabcdeb") == "bcdeb"
assert remove_duplicates("abbddaccaaabcd") == "abcd"
#remove_duplicates("ababcadbka") #doesnt really remove dups
print('all tests have passed!')