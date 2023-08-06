"""
Given an array of numbers sorted in ascending order, find the range of a given number key
The range of the key will be the first and last position in the array

Write a function to return the range of the key. 
If the key is not present return [-1,-1]

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]

O(log N)
"""

def binary_search(arr, key):

    start, end = 0, len(arr) -1

    while start <= end:
        mid = (end - start)//2 + start
        if arr[mid] == key:
            start, end = mid, mid
            while start > 0 and arr[start - 1] == key:
                start = start - 1
            while end < len(arr) - 1 and arr[end + 1] == key:
                end = end + 1
            return [start, end]
        if key < arr[mid]:
            #search lower half
            end = mid - 1
        else:
            #search upper half
            start = mid + 1
    return [-1,-1]
    


assert binary_search([4, 6, 6, 6, 9], key = 6) == [1, 3]
assert binary_search([1, 3, 8, 10, 15], key = 10) == [3,3]
assert binary_search([1, 3, 8, 10, 15], key = 12) == [-1,-1]
print('all tests have passed!')