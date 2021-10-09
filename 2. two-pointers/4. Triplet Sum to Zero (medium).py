"""
***HARD***


Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""

def tripplets(arr, target):
    arr.sort()
    """
    [-3, -2, -1, 0, 1, 1, 2]
    """
    triplets = []
    for i in range(len(arr)):
      if i > 0 and arr[i] == arr[i-1]:
        continue #means its a duplicate
      if i == len(arr) - 1:
        continue # this is end of list
      #X + Y + Z = 0 ==== Y + Z = -X
      triplets = triplets + search_pair(l = arr[i+1:], target = -arr[i])
    print(triplets)
    return triplets



def search_pair(l, target):
  left = 0
  nl = []
  right = len(l) -1
  while left < right:
    ztotal = l[left] + l[right]
    if ztotal == target:
       nl.append([-target, l[left], l[right]])
       left = left + 1
       right = right - 1
       while left < right and l[left] == l[left - 1]:
         left = left + 1
       while left < right and l[right] == l[right + 1]:
         right = right - 1
    elif ztotal > target:
      right = right - 1
    else:
      left = left + 1
  return nl

assert tripplets([-3, 0, 1, 2, -1, 1, -2], 0) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
assert tripplets([-5, 2, -1, -2, 3], 0) == [[-5, 2, 3], [-2, -1, 3]]
print('all tests past!')