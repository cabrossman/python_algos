"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal 
to the sum of the square of all of its digits, leads us to number '1'. 
All other (not-happy) numbers will never reach '1'. 
Instead, they will be stuck in a cycle of numbers which does not include '1'.

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

2^3 + 3^2 == 13
1^2 + 3^2 == 10
1^2 + 0^2 == 1

Input: 12   
Output: false (12 is not a happy number)  
Explanations: Here are the steps to find out that 12 is not a happy number:

Need to find if the constructed list has a cycle
"""
def find_happy_number(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(n)**2 for n in str(num))
    return num == 1

assert find_happy_number(23) == True
assert find_happy_number(12) == False
print('all tests passed!')
