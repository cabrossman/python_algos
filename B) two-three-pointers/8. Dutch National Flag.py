"""
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; 
and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.
"""

def find_subarrays(arr):
  ### Handle edge cases
  if len(arr) <= 1:
    return arr
  if len(arr) == 2:
    if arr[0] > arr[1]:
      return [arr[1], arr[0]]
    else:
      return arr
  
  ### CORE LOGIC
  left, mid, right = 0, 0, len(arr) - 1
  while mid <= right:
    if arr[mid] == 0:
      arr[left], arr[mid] = arr[mid], arr[left]
      left += 1
      mid += 1
    elif arr[mid] == 1:
      mid += 1
    elif arr[mid] == 2:
      arr[right], arr[mid] = arr[mid], arr[right]
      right -= 1
  return arr

assert find_subarrays([1, 0, 2, 1, 0]) == [0, 0, 1, 1, 2]
assert find_subarrays([2, 2, 0, 1, 2, 0]) == [0, 0, 1, 2, 2, 2 ]
print('all tests past!')