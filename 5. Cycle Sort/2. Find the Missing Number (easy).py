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
      first_idx = nums[i]
      if first_idx < n and first_idx != nums[first_idx]:
        second_idx = nums[first_idx]
        nums[i] = second_idx
        nums[first_idx] = first_idx
      else:
        i = i + 1
  for i in range(n):
    if i != nums[i]:
      return i
  return n


assert find_missing_number([4, 0, 3, 1]) == 2
assert find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]) == 7
print('all tests past!')