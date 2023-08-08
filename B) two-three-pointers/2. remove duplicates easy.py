"""
Given an array of sorted numbers, remove all duplicates from it. 
You should not use any extra space; after removing the duplicates 
in-place return the length of the subarray that has no duplicate in it.

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
"""

def main(nums):
    j = 1
    for i in range(1, len(nums)):
        not_dup = nums[i] != nums[i-1]
        if not_dup:
            nums[j] = nums[i]
            j += 1
    return j


assert main([2, 3, 3, 3, 6, 9, 9]) == 4
assert main([2, 2, 2, 11]) == 2
print('all tests past!')