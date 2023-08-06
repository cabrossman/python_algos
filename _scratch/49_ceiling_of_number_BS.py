"""
Given an array of numbers sorted in an ascending order, find the ceiling of a given number key. 
The ceiling of the key will be the smallest element in the given array greater than or equal to the key.

Write a function to return the index of the ceiling of the key. If there isnt any ceiling return -1.

Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

Input: [1, 3, 8, 10, 15], key = 12
Output: 4
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

Input: [4, 6, 10], key = 17
Output: -1
Explanation: There is no number greater than or equal to '17' in the given array.

Input: [4, 6, 10], key = -1
Output: 0
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.

O(log N)
"""

def binary_search(arr, key):
    #start with binary search
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (end - start)//2 + start
        if arr[mid] == key:
            return mid
        if key > arr[mid]:
            start = mid + 1
        else:
            end = mid -1

    #after while loop
    #switch end and start - (break in while)
    start, end = end, start
    #censor end < len()
    end = min(end, len(arr)-1)
    #censor start > 0
    start = max(start,0)
    #if > end -> -1
    if key > arr[end]:
        return - 1 #outside of range
    #if < start -> start (ceiling)
    if key < start:
        return start
    #else return end
    return end

assert binary_search([4, 6, 10], key = 6) == 1
assert binary_search([1, 3, 8, 10, 15], key = 12) == 4
assert binary_search([4, 6, 10], key = 17) == -1
assert binary_search([4, 6, 10], key = -1) == 0
print('all tests have passed!')