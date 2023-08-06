"""
Given an array of unsorted numbers and a target number, 
find a triplet in the array whose sum is as close to the target number as possible, 
return the sum of the triplet. 

If there are more than one such triplet, 
return the sum of the triplet with the smallest sum.

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

"""
import math


def triplet_sum_close_to_target(arr, t):
  arr.sort()
  """
  [-2, 0, 1, 2]
  """
  best_min = math.inf
  for i in range(len(arr) -2): #leave two from right for pointers
    left = i + 1
    right = len(arr) - 1
    while(left < right):
      zsum = arr[i] + arr[left] + arr[right] # for debugging
      diff = t - zsum
      if diff == 0: #they are exactly the same
        return t

      # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
      if abs(diff) < abs(best_min) or (
          abs(diff) == abs(best_min) 
          and 
          diff > best_min
      ):
        best_min = diff  # save the closest and the biggest difference

      if diff > 0:
        left = left + 1
      else:
        right = right - 1
  return t - best_min


assert triplet_sum_close_to_target([-2, 0, 1, 2], t=2) == 1
assert triplet_sum_close_to_target([-3, -1, 1, 2], t=1) == 0
assert triplet_sum_close_to_target([1, 0, 1, 1], t=100) == 3
print('all tests past!')