"""
Find the maximum value in a given Bitonic array. 
An array is considered bitonic if it is monotonically increasing 
and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1]

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Input: [3, 8, 3, 1]
Output: 8

Input: [1, 3, 8, 12]
Output: 12

Input: [10, 9, 8]
Output: 10

O(log N)
"""

def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) -1
    while start <= end:
        mid = (end - start)//2 + start
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]

assert find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]) == 12
assert find_max_in_bitonic_array([3, 8, 3, 1]) == 8
assert find_max_in_bitonic_array([1, 3, 8, 12]) == 12
assert find_max_in_bitonic_array([10, 9, 8]) ==10
print('all tests have passed!')