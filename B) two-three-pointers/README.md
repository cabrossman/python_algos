# 2. Two Pointers

## What is it?
Given lists find a set of elements that fulfil contraints - could be pair, triplet, subarray

Brute force is O(N^2)
This algo is O(N) (sorting is O(N * logN) so its equal to that)

## Why use it?
- Pair equals target, Tripplets equal target, Quadruplets equal target
- Remove Duplicates in place
- Given an array of unsorted numbers, find all unique triplets in it that add up to zero

## Concepts
Given an array of *sorted* numbers and a target sum, find a pair in the array whose sum is equal to the given target.
```
array.sort() # if contain dups
left, right = 0, len(array) #initialize left at 0 and right at length
While left < right:
check if equal to target

If the sum of pointers > target:
- decrement right
Else:
- increment left

Pair Form
- X + Y = Target
- while left < right 

Tripplets (or higher)
- Put in pair form and iterate through each item
- X + Y + Z = Target ==>  Y + Z = (Target - X)
```

## Complexity - Generally
time complexity : O(N) - assumes a sorted list - brute force is O(N^2)
space complexity : O(1) - doesnt store values

## API
```
main(arr, key)
```

## How its done
### Basic Algo - Pair
```
def search_pair(l, target):
  left, right, nl = 0, len(1) -1, []
  while left < right:
    ztotal = l[left] + l[right]
    if ztotal == target:
       nl.append([-target, l[left], l[right]])
       left = left + 1
       right = right - 1
       while left < right and l[left] == l[left - 1]:
         left = left + 1
       while left < right and l[right] == l[right + 1]:
         right = right - 1
    elif ztotal > target:
      right = right - 1
    else:
      left = left + 1
  return nl
```
### Tripplets Sum to Zero
```
def tripplets(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
      if i > 0 and arr[i] == arr[i-1]:
        continue #means its a duplicate
      if i == len(arr) - 1:
        continue # this is end of list
      #X + Y + Z = 0 ==== Y + Z = -X
      triplets = triplets + search_pair(l = arr[i+1:], target = -arr[i])
    print(triplets)
    return triplets
```
### Triplets Core Algo
```
arr.sort()
best_min = math.inf
for i in range(len(arr) -2): #leave two from right for pointers
  left = i + 1
  right = len(arr) - 1
  while(left < right):
    zsum = arr[i] + arr[left] + arr[right] # for debugging
    diff = t - zsum
    if diff == 0: #they are exactly the same
      return t

  ...More stuff..
  
  if diff > 0:
    left = left + 1
  else:
    right = right - 1
```