"""
We are given an array containing 'n' distinct numbers taken from 
the range 0 to 'n'. Since the array has only 'n' numbers out of 
the total 'n+1' numbers, find the missing number.

Input: [4, 0, 3, 1]
Output: 2

Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""

def find_missing_number(nums):
    i, n = 0, len(nums)
    while i < n:
        p1 = nums[i]
        if p1 < n and p1 != nums[p1]: #dont get index error & dont have inf loop
            p2 = nums[p1]
            nums[i] = p2
            nums[p1] = p1
        else:
            i += 1
    for i, val in enumerate(nums):
        if i != val:
            return i

assert find_missing_number([4, 0, 3, 1]) == 2
assert find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]) == 7
print('all tests past!')