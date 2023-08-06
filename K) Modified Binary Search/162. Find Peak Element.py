"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, 
find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly 
greater than a neighbor that is outside the array.
[-inf, 0,1,2, -inf]

You must write an algorithm that runs in O(log n) time.
"""

"""
Questions - what can we assume on the sort?
- not sorted
"""
"""
Psuedo
- brute force
--> if beging or end is greater then return peak
--> iter through num O(N): if any greater than neighbor return

- log(N)

--->
"""
def find_peak(nums):
    if len(nums) < 3:
        return -1
    if nums[0] > nums[1]:
            return 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        return len(nums) - 1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left

"""Tests"""
assert find_peak([1,2,3,1]) == 2
assert find_peak([1,0,3,1]) == 0 #or 2 - peak left
assert find_peak([1,1,1,1]) == -1
