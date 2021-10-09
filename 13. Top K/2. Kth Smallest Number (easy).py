"""
Given an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

Input: [1, 5, 12, 2, 11, 5], K = 4
Output: 5
Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

Input: [5, 12, 11, -1, 12], K = 3
Output: 11
Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].

O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop

MULT = -1 #use 1 for finding largest numbers and -1 for finding smallest


def find_k_largest_numbers(nums, k):
    min_heap = []
    for i in range(k):
        heappush(min_heap, MULT*nums[i]) #store as negatives for finding "smallest"
    
    for i in range(k, len(nums)):
        if MULT*nums[i] > min_heap[0]: #compare with negative
            heappop(min_heap)
            heappush(min_heap, MULT*nums[i])

    return MULT*min_heap[0]



assert find_k_largest_numbers([1, 5, 12, 2, 11, 5], k = 3) == 5
assert find_k_largest_numbers([1, 5, 12, 2, 11, 5], k = 4) == 5
assert find_k_largest_numbers([5, 12, 11, -1, 12], k = 3) == 11
print('all tests have passed!')
