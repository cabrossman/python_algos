"""
Problem Statement:
Given an integer array nums and an integer k, 
return the kth largest element in the array. 

Note that it is the kth largest element in the sorted order, 
not the kth distinct element.
"""
from heapq import heappop, heappush

def klargest(arr, k):
    min_heap = []
    for i, n in enumerate(arr):
        if (i + 1) <= k:
            heappush(min_heap, n)
        if n > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, n)
    return min_heap[0]

assert klargest([3,2,1,5,6,4], k = 2) == 5
assert klargest([3,2,3,1,2,4,5,5,6], k = 4) == 4
assert klargest([-1,2,-8,7,5], k = 3) == 2
print('all tests have passed!')