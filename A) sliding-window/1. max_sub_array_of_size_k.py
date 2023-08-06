"""
Given an array of positive numbers and a positive number K
find the maximum sum of any contiguous subarray of size K

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

O(N)
"""

def max_sub_array_of_size_k(k, arr):
  window_sum, highest_window = 0,0
  for i in range(len(arr)):
    window_sum = window_sum + arr[i]
    if i < (k - 1):
      continue
    if window_sum > highest_window:
      highest_window = window_sum
    window_sum = window_sum - arr[i-(k - 1)]
  return highest_window


assert max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]) == 9
assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7
print('all tests have passed!')