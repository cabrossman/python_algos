"""
We are given an unsorted array containing n numbers taken from the range 1 to n. 
The array has some numbers appearing twice, 
find all these duplicate numbers without using any extra space.

Input: [3, 4, 4, 5, 5]
Output: [4, 5]

Input: [5, 4, 7, 2, 3, 5, 3]
Output: [3, 5]
"""

def find_duplicate(nums):
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
  return dups


assert find_duplicate([3, 4, 4, 5, 5]) == set([4, 5])
assert find_duplicate([5, 4, 7, 2, 3, 5, 3]) == set([3, 5])
print('all tests past!')