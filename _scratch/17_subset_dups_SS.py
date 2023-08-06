"""
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

def find_subsets(nums):
    nums.sort()
    subsets = [[]]
    for j, num in enumerate(nums):
      if j == 0:
        prior = []
        for i in range(len(subsets)):
          subset = list(subsets[i])
          subset.append(num)
          subsets.append(subset)
          prior.append(subset)
      elif nums[j] != nums[j-1]:
        prior = []
        for i in range(len(subsets)):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)
            prior.append(subset)
      else:
        tmp = []
        for i in range(len(prior)):
          subset = list(prior[i])
          subset.append(num)
          subsets.append(subset)
          tmp.append(subset)
        prior = tmp
    return subsets

assert find_subsets([1, 3, 3]) == [[], [1], [3], [1,3], [3,3], [1,3,3]]
assert find_subsets([1, 5, 3, 3]) == [
  [], [1], [3], [1,3],[3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]
]


print('all tests have passed')