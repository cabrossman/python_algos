"""
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.


Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11


"""


def main(l, target):
    left = 0
    right = len(l) - 1
    while right > left:
        if l[left] + l[right] == target:
            return [left, right]
        elif l[left] + l[right] > target:
            right -= 1
        else:
            left += 1
    return 0
            

assert main([1, 2, 3, 4, 6], 6) == [1, 3]
assert main([2, 5, 9, 11], 11) == [0, 2]
print('all tests past!')