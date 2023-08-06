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

def sort_colors(arr):
    """
    Three pointers - left, mid, right
    left = 0, mid = 1, right = len(arr) - 1
    if right = 2 then move left
    if left = 0 then move right
    else move mid right
    if mid == right then move left right and put mid = left + 1
    do while left < right
    """
    left, right = 0, len(arr) - 1
    if len(arr) <= 1:
        return arr
    if len(arr) == 2:
        if arr[0] < arr[1]:
            return arr
        else:
            return [arr[1],arr[0]]
    while left < right:
        while arr[left] == 0: left += 1
        while arr[right] == 2: right -= 1
        if left > right:
            break
        mid = left + 1
        lv, mv, rv = arr[left], arr[mid], arr[right]
        if mv == 0 or rv == 0:
            if mv < rv:
                arr[left], arr[mid] = arr[mid], arr[left]
            else:
                arr[left], arr[right] = arr[right], arr[left]
            left += 1
            mid += 1
        elif lv == 2 or mv == 2:
            if lv > mv:
                arr[right], arr[left] = arr[left], arr[right]
            else:
                arr[right], arr[mid] = arr[mid], arr[right]
            right -= 1
        else: #
            mid += 1
            if mid >= right:
                left += 1
                mid = left + 1
    return arr


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
