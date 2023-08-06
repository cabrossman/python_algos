"""
Given a sorted number array and two integers K and X, 
find K closest numbers to X in the array. 

Return the numbers in the sorted order. X is not necessarily present in the array.

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]

O(log K)
"""

from heapq import heappush, heappop

def find_closest_elements(nums, K, X):
    #store tuple of (dist, num) in min_heap
    min_heap = []
    for num in nums:
        val = (abs(num - X), num)
        heappush(min_heap, val)


    #pop top K from heap and push to "sorted_heap" then return top 3 of those
    result = []
    for _ in range(K):
        (dist, num) = heappop(min_heap)
        result.append(num)
    return sorted(result)

assert find_closest_elements([5, 6, 7, 8, 9], 3, 7) == [6, 7, 8]
assert find_closest_elements([2, 4, 5, 6, 9], 3, 6) == [4, 5, 6]
assert find_closest_elements([2, 4, 5, 6, 9], 3, 10) == [5, 6, 9]
print('all tests have passed!')