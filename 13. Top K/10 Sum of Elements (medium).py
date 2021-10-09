"""
Given an array, find the sum of all numbers between the K1th 
and K2th smallest elements of that array.

Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
Output: 23
Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
between 5 and 15 is 23 (11+12).

Input: [3, 5, 8, 7], and K1=1, K2=4
Output: 12
Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
number (8) is 12 (5+7).

O(N log K + K log K)
"""

from heapq import heappush, heappop

def find_sum_of_elements(nums, k1, k2):
  # insert all numbers into min_heap
  min_heap = []
  for num in nums:
    heappush(min_heap, num)

  #remove k1 numbers from heap
  for _ in range(k1):
    heappop(min_heap)

  #sum from k1 to k2
  return sum(heappop(min_heap) for _ in range(k2 - k1 - 1))


assert find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6) == 23
assert find_sum_of_elements([3, 5, 8, 7], 1, 4) == 12
print('all tests have passed!')