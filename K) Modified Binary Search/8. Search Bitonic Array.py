"""
Given a Bitonic array, find if a given key is present in it. 
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the key. If the key is not present, return -1.

Input: [1, 3, 8, 4, 3], key=4
Output: 3

Input: [3, 8, 3, 1], key=8
Output: 1

Input: [1, 3, 8, 12], key=12
Output: 3

Input: [10, 9, 8], key=10
Output: 0

O(log N)
"""

def search_bitonic_array(arr, key):
    start, end = 0, len(arr) -1
    while start <= end:
        mid = (end - start)//2 + start
        val = arr[mid]
        if val == key:
            return mid
        if mid < len(arr) - 1:
            increasing = val < arr[mid + 1]
        else:
            increasing = False
        if increasing:
            if key > val:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if key < val:
                start = mid + 1
            else:
                
                end = mid - 1
    return -1

assert search_bitonic_array([1, 3, 8, 4, 3], 4) == 3
assert search_bitonic_array([3, 8, 3, 1], 8) == 1
assert search_bitonic_array([1, 3, 8, 12], 12) == 3
assert search_bitonic_array([10, 9, 8], 10) == 0
assert search_bitonic_array([6,7,1,2,3,4,5], 2) == 3
assert search_bitonic_array([10,11,12,13,1,2,3], 12) == 2
print('all tests have passed!')