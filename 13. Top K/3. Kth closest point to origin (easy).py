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

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.dist_from_origin < other.dist_from_origin

    @property    
    def dist_from_origin(self):
        return sqrt((self.x - 0)**2 + (self.y - 0)**2)


class hPoint(Point):
    def __lt__(self, other):
        """
            The largest distinace from the origin in the heap
            is the first one to discard. 
        """
        return self.dist_from_origin > other.dist_from_origin



def find_closest_points(points, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, points[i]) 
    
    for i in range(k, len(points)):
        # check distance from origin as candidate for heap
        if points[i].dist_from_origin < min_heap[0].dist_from_origin: 
            #heap uses __lt__ method to add largest distance from org in heap as new head
            heappop(min_heap)
            heappush(min_heap, points[i])

    return [[p.x, p.y] for p in list(min_heap)]



assert find_closest_points([hPoint(1, 2), hPoint(1, 3)], k = 1) == [[1,2]]
assert find_closest_points([hPoint(1, 3), hPoint(3, 4), hPoint(2, -1)], 2) == [[1, 3], [2, -1]]
print('all tests have passed!')
