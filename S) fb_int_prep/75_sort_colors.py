"""
You are given an array with n objects colored red, white, or blue, 
sorted them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the 
color red, white, and blue, respectively.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


You are not supposed to use the library's sort function for this problem.
You should do it in-place without making a copy of the array.
"""


def sortColors(nums):
    low=mid=0
    high=len(nums)-1
    while mid<=high:
        if nums[mid]==0:
            nums[low],nums[mid]=nums[mid],nums[low]
            low+=1
            mid+=1
        elif nums[mid]==1:
            mid+=1
        else:
            nums[mid],nums[high]=nums[high],nums[mid]
            high-=1
    return nums

assert sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2]
assert sortColors([2,2,1]) == [1,2,2]
assert sortColors([1]) == [1]
assert sortColors([]) == []
assert sortColors([0,0,0,1,1,2,2,2]) == [0,0,0,1,1,2,2,2]
assert sortColors([2,0,1,0,2,1,0]) == [0,0,0,1,1,2,2]
assert sortColors([1,2,0,2,1,0,1,2,0,2]) == [0,0,0,1,1,1,2,2,2,2]
print('all tests have passed!')
