"""
There are n buildings in a line. 
You are given an integer array heights of size n 
that represents the heights of the buildings in the line.

The ocean is to the right of the buildings. 
A building has an ocean view if the building can see 
the ocean without obstructions. Formally, a building has an 
ocean view if all the buildings to its right have a smaller height.

Return a list of indices (0-indexed) of buildings that have an ocean view, 
sorted in increasing order.

Input: heights = [4,2,3,1]
Output: [0,2,3]

Input: heights = [4,3,2,1]
Output: [0,1,2,3]

Input: heights = [1,3,2,4]
Output: [3]

Input: heights = [2,2,2,2]
Output: [3]
"""
from collections import deque
def ocean_view(heights):
    max_height = 0
    out = deque()
    for i in range(len(heights)-1,-1,-1):
        if i == len(heights) -1:
            max_height = max(max_height, heights[i])
            out.appendleft(i)
        elif heights[i] > max_height:
            max_height = max(max_height, heights[i])
            out.appendleft(i)
    return list(out)


assert ocean_view([4,2,3,1]) == [0,2,3]
assert ocean_view([4,3,2,1]) == [0,1,2,3]
assert ocean_view([1,3,2,4]) == [3]
assert ocean_view([2,2,2,2]) == [3]
print('all tests passed!')