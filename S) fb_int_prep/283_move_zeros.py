"""
Here's the description of the problem:

Given an integer array nums, move all 
0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
def move0(arr):
    i = 0
    for num in arr:
        if num != 0:
            arr[i] = num
            i += 1
    while i < len(arr):
        arr[i] = 0
        i += 1
    return arr

assert move0([0,2,1,0,9,3]) == [2,1,9,3,0,0]
print('all tests passed!')