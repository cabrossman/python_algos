"""
Given an array of points in a 2D plane, find K closest points to the origin

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]

O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop
from math import sqrt

def find_closest_points(points, k):
    min_heap = []
    for point in points:
        dist = sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
        tup = (dist, point[0], point[1])
        heappush(min_heap, tup)

    res = []
    for _ in range(k):
        p = heappop(min_heap)
        res.append([p[1], p[2]])
    return res


assert find_closest_points([(1, 2), (1, 3)], k = 1) == [[1,2]]
assert find_closest_points([(1, 3), (3, 4), (2, -1)], 2) == [[2, -1], [1, 3]]
print('all tests have passed!')
