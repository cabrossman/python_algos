"""
In a non-empty array of integers, 
every number appears twice except for one, 
find that single number.

Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Input: 7, 9, 7
Output: 9
"""
from functools import reduce

def find_single_number(arr):
  return reduce(lambda x, y: x ^ y, arr)

assert find_single_number([1,4,2,1,3,2,3]) == 4
print('all tests have passed')