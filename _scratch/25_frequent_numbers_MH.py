"""
Given an unsorted array of numbers, find the top K frequently occurring numbers in it.

Input: [1, 3, 5, 12, 11, 12, 11], K = 2
Output: [12, 11]
Explanation: Both '11' and '12' apeared twice.

Input: [5, 12, 11, 3, 11], K = 2
Output: [11, 5] or [11, 12] or [11, 3]
Explanation: Only '11' appeared twice, all other numbers appeared once.

O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop

def find_k_frequent_numbers(nums, k):

    cnts = {}
    for num in nums:
        cnts[num] = cnts.get(num,0) + 1

    max_heap = [] 
    for num_idx, freq in cnts.items():
        heappush(max_heap, (-freq, num_idx))

    out = []
    for i in range(k):
        (_, num_idx) = heappop(max_heap)
        out.append(num_idx)
    return out

assert find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], k = 2) == [11, 12]
assert find_k_frequent_numbers([5, 12, 11, 3, 11], k = 2) in [[11,5], [11, 12], [11,5], [11,3]]
print('all tests have passed!')
