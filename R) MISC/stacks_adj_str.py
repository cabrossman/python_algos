
def remove_duplicates(string):
    # Create an empty stack.
    stack = []
    # Iterate over the string
    for char in string:
        # If stack has at least one character and
        # stack's top character is same as the string's character
        if stack and stack[-1] == char:
            # Pop a character from the stack.
            stack.pop()
        else:
            # Otherwise, push that character onto the stack.
            stack.append(char)
    
    # Form a string from stack's elements and return that.
    return "".join(stack)

assert remove_duplicates('g') == 'g'
assert remove_duplicates("ggaabcdeb") == "bcdeb"
assert remove_duplicates("abbddaccaaabcd") == "abcd"
#remove_duplicates("ababcadbka") #doesnt really remove dups
print('all tests have passed!')