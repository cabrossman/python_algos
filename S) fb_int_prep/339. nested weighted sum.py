"""
Given a nested list of integers, 
return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list 
-- whose elements may also be integers or other lists.

Example 1: Given the list [[1,1],2,[1,1]], return 10. 
(four 1's at depth 2, one 2 at depth 1)

Example 2: Given the list 
[1,[4,[6]]], return 27. 
(one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4 * 2 + 6 * 3 = 27)
"""
def wsum(nums, depth = 1, tot = 0):
    for num in nums:
        if isinstance(num, list):
            tot += wsum(num, depth + 1, tot = 0)
        else:
            tot += (num * depth)
    return tot

assert wsum([[1,1],2,[1,1]]) == 10
assert wsum([1,[4,[6]]]) == 27
print('all tests have passed!')