# 11. Modified Binary Search

## What is it?
This pattern describes an efficient way to handle all problems involving searching for a key in a sorted list.

Time Complexity : O(log N)

## Why use it?
- Find k in array. We know its sorted but not sure which direction
- Regardless of order
- Ceiling of number
- Smallest letter in the given array greater than key
- Duplicate numbers
- Infinite Array 
- Closest to key (difference)
- Bitonic array : [1, 3, 8, 12, 4, 2]

## Concepts

- start & end : lower & upper limits to search
- mid : midway between start and end to test. 

## Complexity - Generally
- Time Complexity: O(log N)
- Auxiliary Space: O(1)

## API
```
binary_search(arr, key)
```

## How its done
### Basic Algo
```
def binary_search(arr, key):
    start, end = 0, len(arr) -1
    while start <= end:
        mid = (end - start)//2 + start
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid - 1 #search lower half
        else:
            start = mid + 1 #search upper half
```
## Variants
### Find Index of closest number greater than mid
```
    start, end = end, start #at end of Binary Search they are swapped
    end = end if end < len(arr) - 1 else len(arr) - 1
    start = start if start >= 0 else 0
    if key > arr[end]:
        return -1
    if key < arr[start]:
        return start
    return end
```
### If not sure of ASC or DESC order
```
if ASC_ORDER:
    if arr[mid] > key:
else:
    if arr[mid] < key:
```
### Next Letter
```
idx = start % len(arr)
return arr[idx]
```
### Duplicates
```
if arr[mid] == key:
    start, end = mid, mid
    while start > 0 and arr[start - 1] == key:
        start = start - 1
    while end < len(arr) - 1 and arr[end + 1] == key:
        end = end + 1
    return [start, end]
```
### Infinite Array
```
def search_in_infinite_array(reader, key):
    start, end = 0,1
    while reader.get(end) < key:
        start = end + 1
        end = (end + 1)*2
```
### Bitonic Array
```
def find_max_in_bitonic_array(arr):
    start, end = 0, len(arr) -1
    while start < end:
        mid = (end - start)//2 + start
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]
```