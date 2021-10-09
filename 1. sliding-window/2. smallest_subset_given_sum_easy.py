"""
Given an array of positive numbers and a positive number 'S,'
find the length of the smallest contiguous subarray whose 
sum is greater than or equal to 'S'. Return 0 if no such subarray exists.

Input: [2, 1, 5, 2, 3, 2], S=7 
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

Input: [2, 1, 5, 2, 8], S=7 
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Input: [3, 4, 1, 1, 6], S=8 
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] 
or [1, 1, 6].

"""

def main(l,s):
  window_sum = 0
  window_start = 0
  smallest_sub_array = len(l)
  for window_end in range(len(l)):
    window_sum = window_sum + l[window_end]
    while window_sum >= int(s):
      smallest_sub_array = min(smallest_sub_array, window_end - window_start + 1)
      window_sum = window_sum - l[window_start]
      window_start = window_start + 1
  return smallest_sub_array


assert main([2, 1, 5, 2, 3, 2],'7') == 3
assert main([2, 1, 5, 2, 8], '7') == 1
assert main([3, 4, 1, 1, 6], 8) == 3

print('all tests past!')


