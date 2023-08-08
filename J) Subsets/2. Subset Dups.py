"""
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

def find_subsets(nums):
  #its like subsets - only when we find a duplicate
  # we only append to the "last" values added to the subsets
  ## IE if we added [1, 3] [3] to the subsets last round this round
  ## we'd add [1, 3, 3] and [3, 3] - for the "3" dup
  nums.sort()
  subsets = [[]]
  for i in range(len(nums)):
    start = 0
    if i > 0 and nums[i] == nums[i-1]:
      start = end
    end = len(subsets)
    for j in range(start, end):
      subset = list(subsets[j])
      subset.append(nums[i])
      subsets.append(subset)
  return subsets


assert find_subsets([1, 3, 3]) == [[], [1], [3], [1,3], [3,3], [1,3,3]]
assert find_subsets([1, 5, 3, 3]) == [
  [], [1], [3], [1,3],[3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]
]


print('all tests have passed')