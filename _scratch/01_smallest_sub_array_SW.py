"""
Given an array of positive numbers and a positive number K
find the maximum sum of any contiguous subarray of size K

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

O(N)
"""

def max_sub_array_of_size_k(k, arr):
    window_sum, highest_sum = 0,0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i + 1) < k:
            continue
        if window_sum > highest_sum:
            highest_sum = window_sum
        window_sum -= arr[(i+1) - k] #remove last item
    return highest_sum

assert max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]) == 9
assert max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]) == 7
print('all tests have passed!')