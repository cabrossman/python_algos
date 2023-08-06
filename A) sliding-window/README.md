# 1. Sliding Window

## What is it?
Given an array, find the average/sum of all contiguous subarrays of size K in it. Could be variable window size

## Why use it?
- Given an array of positive numbers and a positive number S,find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists.
- Given a string, find the length of the longest substring in it with no more than K distinct characters.

## Concepts
- **Sliding Window** : Calulate the sum of the previous subarray. To slide window forward subtract element going out from sum and add element comming in. It reduces the time from O(N*K) to O(N)

## Complexity - Generally
time complexity : O(N)
space complexity : O(1) - doesnt store values

## API
```
main(arr, key)
```

## How its done
### Basic Algo
```
def max_sub_array_of_size_k(k, arr):
  window_sum, highest_window = 0,0
  for i in range(len(arr)):
    window_sum = window_sum + arr[i]
    if i < (k - 1):
      continue
    if window_sum > highest_window:
      highest_window = window_sum
    window_sum = window_sum - arr[i-(k - 1)]
  return highest_window
```

### Variable Window Size
The while statement allows a flexible window size. It shrinks the window start
```
def main(l,s):
  window_sum, window_start  = 0, 0
  smallest_sub_array = len(l)
  for window_end in range(len(l)):
    window_sum = window_sum + l[window_end]
    while window_sum >= s:
      smallest_sub_array = min(smallest_sub_array, window_end - window_start + 1)
      window_sum = window_sum - l[window_start]
      window_start = window_start + 1
  return smallest_sub_array
```