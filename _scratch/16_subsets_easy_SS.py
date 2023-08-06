"""
Given a set with distinct elements, find all of its distinct subsets.

Input: [1, 3]
Output: [], [1], [3], [1,3]

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

def find_subsets(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)
    return subsets

assert find_subsets([1, 3]) == [[], [1], [3], [1, 3]]
assert find_subsets([1, 5, 3]) == [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]
print('all tests have passed')