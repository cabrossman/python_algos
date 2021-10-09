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
    ### map counter
    m = {}
    for num in nums:
        m[num] = m.get(num,0) + 1

    ##heap with top k counts
    ### all smallest numbers get popped
    min_heap = []
    for num,counter in m.items():
        heappush(min_heap, (counter,num))
        if len(min_heap) > k:
            heappop(min_heap)


    ### return top 2 counts in list
    return sorted([l[1] for l in list(min_heap)])



assert find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], k = 2) == [11, 12]
assert find_k_frequent_numbers([5, 12, 11, 3, 11], k = 2) in [[5,11], [11, 12], [3, 11]]
print('all tests have passed!')
