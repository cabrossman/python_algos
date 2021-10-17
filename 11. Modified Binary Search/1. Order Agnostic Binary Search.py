"""
Problem Statement #
Given a sorted array of numbers, find if a given number key is present in the array. 
Though we know that the array is sorted, we dont know if its sorted in ascending or descending order. 
You should assume that the array can have duplicates.

Write a function to return the index of the key if it is present in the array, otherwise return -1.

Input: [4, 6, 10], key = 10
Output: 2

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4

Input: [10, 6, 4], key = 10
Output: 0

Input: [10, 6, 4], key = 4
Output: 2

O(log N)
"""

def binary_search(arr, key):

    start, end = 0, len(arr) -1
    ASC_ORDER = True if arr[0] < arr[-1] else False

    while start <= end:
        mid = (end - start)//2 + start
        if arr[mid] == key:
            return mid

        if ASC_ORDER:
            if arr[mid] > key:
                end = mid - 1 #search lower half
            else:
                start = mid + 1 #search upper half
        else:
            if arr[mid] < key:
                end = mid - 1 #search lower half
            else:
                start = mid + 1 #search upper half
    return -1


assert binary_search([4, 6, 10], 10) == 2
assert binary_search([1, 2, 3, 4, 5, 6, 7], 5) == 4
assert binary_search([10, 6, 4], 10) == 0
assert binary_search([10, 6, 4], 4) == 2
print('all tests have passed!')