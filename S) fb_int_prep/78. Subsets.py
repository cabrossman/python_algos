"""
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""

def compute(nums):
    subsets = [[]]
    for num in nums:
        for i in range(len(subsets)):
            subset = list(subsets[i])
            subset.append(num)
            subsets.append(subset)
    return subsets

assert compute([1,2,3]) == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
assert compute([0]) == [[],[0]]
print('all tests passed!')