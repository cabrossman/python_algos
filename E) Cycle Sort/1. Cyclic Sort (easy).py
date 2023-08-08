"""
We are given an array containing n objects. 
Each object, when created, was assigned a unique number 
from the range 1 to n based on their creation sequence. 
This means that the object with sequence number 3 was created 
just before the object with sequence number 4.

Write a function to sort the objects in-place on their 
creation sequence number in O(n) and without using any extra space. 
For simplicity, let's assume we are passed an integer array 
containing only the sequence numbers, though each number is actually an object.

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]
"""

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    p1 = nums[i]
    p2 = nums[p1 - 1]
    nums[i], nums[p1 - 1] = p2, p1
    if (i + 1) == nums[i]:
        i += 1
  return nums


assert cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
assert cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
assert cyclic_sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]
print('all tests past!')