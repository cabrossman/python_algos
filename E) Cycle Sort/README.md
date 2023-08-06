# 5. Cycle Sort

## What is it?
You are given an unsorted array containing n numbers taken from the range 1 to n. The array can have duplicates, which means that some numbers will be missing. Find all the missing numbers.

To efficiently solve this problem, we can use the fact that the input array contains numbers in the range of 1 to n. For example, to efficiently sort the array, we can try placing each number at its correct place, i.e., placing 1 at index '0', placing 2 at index '1', and so on. Once we are done with the sorting, we can iterate the array to find all indices missing the correct numbers. These will be our required numbers.

Time Complexity : Brute Force O(N^2) to O(N) == O(N) + O(N-1)

## Why use it?
- Sort Numbers
- Find Missing Number(s)
- Find Duplicate Number(s)

## Concepts
- Numbers must range from 1 to n. Numbers are swapped to their corresponding index value. IE 5 goes to (5-1) index
- Will swap numbers to their place until first and second digit are in place. If a number is in the correct location no swap occurs
- i = 0; While i < len(nums) -> increment i when index i + 1 in correct location
- Does number start from 0 or 1?

## Complexity - Generally
time complexity : O(N) == O(N) + O(N-1) from Brute Force of O(N^2)
space complexity : O(1)

## API
```
main(nums) #to merge itself
```

## How its done
### Basic Algo - put number in correct locaiton 
```
def cyclic_sort(nums):
  i, n = 0, len(nums)
  while i < n:
      first_idx = nums[i]
      second_idx = nums[first_idx - 1]
      nums[i] = second_idx
      nums[first_idx - 1] = first_idx
      if i + 1 == second_idx:
          i = i + 1
  return nums
```
### Find Missing Number
when number is missing some number will be out of order
return i when you find the error
```
  i, n = 0, len(nums)
  while i < n:
      first_idx = nums[i]
      if first_idx < n and first_idx != nums[first_idx]:
        second_idx = nums[first_idx]
        nums[i] = second_idx
        nums[first_idx] = first_idx
      else:
        i = i + 1
  #Check for missing
  for i in range(n):
    if i != nums[i]:
      return i
  return n
```
### Find all missing numbers
return list of missing numbers when they dont match
```
for i in range(n):
    if i+1 != nums[i]:
        l.append(i+1) #adjustment
return l
```
### Find Duplicates
```
def find_duplicate(nums):
  i, n = 0, len(nums)
  while i < n:
    if i + 1 != nums[i]:
      first_idx = nums[i]
      if first_idx == nums[first_idx - 1]:
        return first_idx
      else: #swap
        second_idx = nums[first_idx - 1]
        nums[i] = second_idx
        nums[first_idx - 1] = first_idx
    else:
      i = i + 1
  return -1
```