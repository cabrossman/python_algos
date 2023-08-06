# 13. Top K

## What is it?
Find the smallest element or largest K element or most frequent. 

Time Complexity :  O(K * log K + (N - K) * log K)

## Why use it?
- Given an unsorted array of numbers, find the K largest numbers in it.
- Given an unsorted array of numbers, find Kth smallest number in it.
- Given an array of points in a 2D plane, find K closest points to the origin
- Given N ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal to the sum of their lengths.
- Given an unsorted array of numbers, find the top K frequently occurring numbers in it.
- Given a string, sort it based on the decreasing frequency of its characters.
- Design a class to efficiently find the Kth largest element in a stream of numbers.
- Given a sorted number array and two integers K and X, find K closest numbers to X in the array. 
- Given an array of numbers and a number K, we need to remove K numbers from the array such that we are left with maximum distinct numbers.
- Given an array, find the sum of all numbers between the K1th and K2th smallest elements of that array.

## Concepts
- Heap data structure

## Complexity - Generally
- Time Complexity: O(N log K)
- Auxiliary Space:  O(K)


## API
```
find_k_frequent_numbers(nums, k)
```

## How its done
### Add all elements to heap
```
from heapq import heappush, heappop
min_heap = []
for i in range(k):
    heappush(min_heap, nums[i])
```
### Check if query number to heaphead and add/push
```
for i in range(k, len(nums)):
    if nums[i] > min_heap[0]:
        heappop(min_heap)
        heappush(min_heap, nums[i])
```
## VARIANTS
### if looking for largest number store & compare numbers in heap negatively
```
# store
heappush(min_heap, -nums[i]) #store as negatives for finding "smallest"
# compaare
if -nums[i] > min_heap[0]: #compare with negative
```

### If designing custom object create a `__lt__` method to compare for heap
```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.dist_from_origin < other.dist_from_origin
```
### Use Map to find how frequent
```
m = {}
for num in nums:
    m[num] = m.get(num,0) + 1

min_heap = []
for num,counter in m.items():
    ### Tuple with count first is stored in order ###
    heappush(min_heap, (counter,num)) 
    if len(min_heap) > k:
        heappop(min_heap)
```
### Check out 7th for stream, 9th for distinct & 10th for sum