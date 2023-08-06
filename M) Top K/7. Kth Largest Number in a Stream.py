"""
Design a class to efficiently find the Kth largest element in a stream of numbers.

The class should have the following two things:

1. The constructor of the class should accept an integer array 
    containing initial numbers from the stream and an integer K.
2. The class should expose a function add(int num) 
    which will store the given number and return the Kth largest number.

Input: [3, 1, 5, 12, 2, 11], K = 4
1. Calling add(6) should return '5'.
2. Calling add(13) should return '6'.
2. Calling add(4) should still return '6'.

O(log K)
"""

from heapq import heappush, heappop

class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []
        for num in nums:
            _ = self.add(num)


    def add(self, num):
        heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]



kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
assert kthLargestNumber.add(6) == 5
assert kthLargestNumber.add(13) == 6
assert kthLargestNumber.add(4) == 6
print('all tests have passed!')