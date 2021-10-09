"""
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

"""
import math

def triplet_with_smaller_sum(arr, t):
  arr.sort()
  triplets = []

  for i in range(len(arr) -2): #leave two from right for pointers
    left = i + 1 
    right = len(arr) - 1
    while(left < right):
      array = [arr[i], arr[left], arr[right]]
      zsum = sum(array) # for debugging
      diff = t - zsum
      tmp_right = right

      #double check indicies arent the same
      while (i != left and i != right and left != right) and diff > 0:
        triplets.append(array)

        #if this diff passes so do all diffs below
        right = right - 1
        array = [arr[i], arr[left], arr[right]]
        zsum = sum(array) # for debugging
        diff = t - zsum
      right = tmp_right #put back to prior than loop
      if diff > 0:
        left = left + 1
      else:
        right = right - 1
  print(triplets)
  return len(triplets)

assert triplet_with_smaller_sum([-1, 0, 2, 3], t=3) == 2
assert triplet_with_smaller_sum([-1, 4, 2, 1, 3], t=5) == 4
print('all tests past!')