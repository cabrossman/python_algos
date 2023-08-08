"""
Given an array of numbers sorted in ascending order, 
find the element in the array that has the minimum difference 
with the given key

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 

Input: [4, 6, 10], key = 4
Output: 4

Input: [1, 3, 8, 10, 15], key = 12
Output: 10

Input: [4, 6, 10], key = 17
Output: 10

O(log N)
"""

def search_min_diff_element(arr, key):
    start, end = 0, len(arr) -1
    while start <= end:
        mid = (end - start)//2 + start
        if key > arr[mid]:
            start = mid + 1
        elif key < arr[mid]:
            end = mid - 1
        else:
            return arr[mid]

    
    end = start # swap for debugging
    end = end if end < len(arr) - 1 else len(arr) - 1 #CLIP it
    start = end - 1 #make start one less

    start_diff = abs(key - arr[start])
    end_diff = abs(key - arr[end])
    if start_diff < end_diff:
        return arr[start]
    else:
        return arr[end]

assert search_min_diff_element([4, 6, 10], 7) == 6
assert search_min_diff_element([4, 6, 10], 4) == 4
assert search_min_diff_element([1, 3, 8, 10, 15], 12) == 10
assert search_min_diff_element([4, 6, 10], 17) == 10
print('all tests have passed!')