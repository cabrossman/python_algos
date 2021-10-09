"""
Given an unsorted array of numbers, find the K largest numbers in it.

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]

O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop


def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return sorted(list(min_heap))



assert find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3) == [5, 11, 12]
assert find_k_largest_numbers([5, 12, 11, -1, 12], 3) == [11, 12, 12]
assert find_k_largest_numbers([100, 100, 2, 50, 49], 3) == [50, 100, 100]
print('all tests have passed!')
