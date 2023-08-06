"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. 
For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has 'n' distinct elements it will have n! permutations.

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

complexity = O(N*N!)
"""

from collections import deque

def find_permutations(nums):
    res = []
    perms = deque()
    perms.append([])
    for num in nums:
        for _ in range(len(perms)):
            permA = perms.popleft()
            for i in range(len(permA) + 1):
                permB = list(permA)
                permB.insert(i, num)
                if len(permB) == len(nums):
                    res.append(permB)
                else:
                    perms.append(permB)
    return res




assert find_permutations([1, 3, 5]) == [
    [5,3,1],
    [3,5,1],
    [3,1,5],
    [5,1,3],
    [1,5,3],
    [1,3,5]
]

print("all tests have passed!")