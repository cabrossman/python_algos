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
    for i, num in enumerate(nums):
        if i <= (k - 1):
            heappush(min_heap, num)
        elif num > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, num)

    return sorted(list(min_heap))


def find_k_smallest_numbers(nums, k):
    max_heap = []
    for i, num in enumerate(nums):
        if i <= (k - 1):
            heappush(max_heap, -num)
        elif max_heap[0]*-1 > num:
            heappop(max_heap)
            heappush(max_heap, -num)

    return -max_heap[0]



assert find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3) == [5, 11, 12]
assert find_k_largest_numbers([5, 12, 11, -1, 12], 3) == [11, 12, 12]
assert find_k_largest_numbers([100, 100, 2, 50, 49], 3) == [50, 100, 100]
print('all tests have passed!')

assert find_k_smallest_numbers([1, 5, 12, 2, 11, 5], k = 3) == 5
assert find_k_smallest_numbers([1, 5, 12, 2, 11, 5], k = 4) == 5
assert find_k_smallest_numbers([5, 12, 11, -1, 12], k = 3) == 11
print('all tests have passed!')
