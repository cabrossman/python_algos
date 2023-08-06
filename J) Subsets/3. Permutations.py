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
    result = []
    permutations = deque()
    permutations.append([])
    for i in range(len(nums)): # on the last iteration everything is added to result
        for _ in range(len(permutations)): #later we add to permutation
            # we pop to mutate the list in the deque
            permutation_A = permutations.popleft() #this saves the n-1 version to add to list later
            #need one more than n which only has 2 in the example to get all permutations
            for j in range(len(permutation_A) + 1): 
                permutation_B = list(permutation_A)
                permutation_B.insert(j, nums[i]) #we insert the nth number at each possible position
                if len(permutation_B) == len(nums): ### must have all numbers and add to result
                    result.append(permutation_B)
                else:
                    permutations.append(permutation_B) ###intermediatery
    return result

assert find_permutations([1, 3, 5]) == [
    [5,3,1],
    [3,5,1],
    [3,1,5],
    [5,1,3],
    [1,5,3],
    [1,3,5]
]

print("all tests have passed!")