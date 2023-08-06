"""
Given an array with positive numbers and a positive target number, 
find all of its contiguous subarrays whose product is less than the target number.

Input: [2, 5, 3, 10], target=30 
Output: [2], [5], [2, 5], [3], [5, 3], [10]
Explanation: There are six contiguous subarrays whose product is less than the target.

Input: [8, 2, 6, 5], target=50 
Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
Explanation: There are seven contiguous subarrays whose product is less than the target.
"""
import math
import functools

def find_subarrays(arr, t):
  arr.sort()
  
  return -1

assert find_subarrays([2, 5, 3, 10], t=30) == [[2], [5], [2, 5], [3], [5, 3], [10]]
assert find_subarrays([8, 2, 6, 5], t=50) == [[8], [2], [8, 2], [6], [2, 6], [5], [6, 5]]
print('all tests past!')