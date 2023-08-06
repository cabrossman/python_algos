"""
We are given an unsorted array containing n+1 numbers taken from the range 1 to n. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

Input: [1, 4, 4, 3, 2]
Output: 4

Input: [2, 1, 3, 3, 5, 4]
Output: 3

Input: [2, 4, 1, 4, 4]
Output: 4
"""

def find_duplicate(nums):
    #starts at 1 - so i = (i + 1) value
    i, n = 0, len(nums)
    while i < n:
      if (i + 1) == nums[i]:
         i = i + 1
      else:
         p1 = nums[i]
         if p1 == nums[p1 - 1]: #dup
            return p1
         else: #swap and continue
            p2 = nums[p1 - 1]
            nums[i] = p2
            nums[p1 - 1] = p1
    return 0

assert find_duplicate([1, 4, 4, 3, 2]) == 4
assert find_duplicate([2, 1, 3, 3, 5, 4]) == 3
assert find_duplicate([2, 4, 1, 4, 4]) == 4
print('all tests past!')