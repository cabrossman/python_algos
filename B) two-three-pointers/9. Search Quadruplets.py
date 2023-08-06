"""
Given an array of unsorted numbers and a target number, 
find all unique quadruplets in it, whose sum is equal to the target number.


Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""
def search_quadruplets(arr, target):
  quadruplets = set()
  arr.sort()
  for i in range(len(arr) - 3):
    for j in range(i + 1,len(arr) - 2):
      left = j + 1
      right = len(arr) - 1
      while(left < right):
        quadruplet = (arr[i], arr[j], arr[left], arr[right])
        if quadruplet in quadruplets:
          left = left + 1
          continue
        _sum = sum(quadruplet)
        if _sum == target:
          quadruplets.add(quadruplet)
          left = left + 1
        elif _sum < target:
          left = left + 1
        else:
          right = right - 1
  return quadruplets

assert search_quadruplets([4, 1, 2, -1, 1, -3], target=1) == {(-3, -1, 1, 4), (-3, 1, 1, 2)}
assert search_quadruplets([2, 0, -1, 1, -2, 2], target=2) == {(-2, 0, 2, 2), (-1, 0, 1, 2)}
print("all tests past!")