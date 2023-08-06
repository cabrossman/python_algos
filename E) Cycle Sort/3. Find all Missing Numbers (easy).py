"""
We are given an unsorted array containing numbers taken from the range 1 to 'n'.
The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

Input: [2, 4, 1, 2]
Output: 3

Input: [2, 3, 2, 1]
Output: 4
"""

def find_missing_numbers(nums):
  i, n = 0, len(nums)
  while i < n:
      first_idx = nums[i]
      if first_idx <= n and first_idx != nums[first_idx - 1]:
        second_idx = nums[first_idx - 1]
        nums[i] = second_idx
        nums[first_idx - 1] = first_idx
      else:
        i = i + 1
  l = []
  for i in range(n):
    if i+1 != nums[i]:
      l.append(i+1)
  return l


assert find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7]
assert find_missing_numbers([2, 4, 1, 2]) == [3]
assert find_missing_numbers([2, 3, 2, 1]) == [4]
print('all tests past!')