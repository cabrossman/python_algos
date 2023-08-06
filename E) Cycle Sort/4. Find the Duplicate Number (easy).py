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
  #starts at 1 so we index up in all cases = (i + 1)
  i, n = 0, len(nums)
  while i < n:
    if (i + 1) != nums[i]: #if index is NOT already in correct spot
      first_idx = nums[i]
      if first_idx == nums[first_idx - 1]: # if a correct number already exists there
        return first_idx
      else: #swap / cycle sort
        second_idx = nums[first_idx - 1]
        nums[i] = second_idx
        nums[first_idx - 1] = first_idx
    else:
      i = i + 1
  return -1


assert find_duplicate([1, 4, 4, 3, 2]) == 4
assert find_duplicate([2, 1, 3, 3, 5, 4]) == 3
assert find_duplicate([2, 4, 1, 4, 4]) == 4
print('all tests past!')