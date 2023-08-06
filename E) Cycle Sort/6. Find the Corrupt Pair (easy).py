"""
Find the Corrupt Pair (easy)#
We are given an unsorted array containing n numbers taken from the range 1 to n. 
The array originally contained all the numbers from 1 to n, 
but due to a data error, one of the numbers got duplicated 
which also resulted in one number going missing. Find both these numbers.

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""

def find_corrupt_numbers(nums):
  i, n = 0, len(nums)
  dups = set()
  while i < n:
    if i + 1 != nums[i]:
      first_idx = nums[i]
      if first_idx == nums[first_idx - 1]:
        dups.add(first_idx)
        i = i + 1
        continue
      else:
        second_idx = nums[first_idx - 1]
        nums[i] = second_idx
        nums[first_idx - 1] = first_idx
    else:
      i = i + 1

  missing = set()
  for i in range(n):
    if i+1 != nums[i]:
      missing.add(i+1)
  return dups | missing



assert find_corrupt_numbers([3, 1, 2, 5, 2]) == set([2,4])
assert find_corrupt_numbers([3, 1, 2, 3, 6, 4]) == set([3, 5])
print('all tests past!')