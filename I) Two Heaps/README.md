# 9. Two Heaps

## What is it?
As the name suggests, this pattern uses two Heaps; A Min Heap to find the smallest element and a Max Heap to find the biggest element.

In many problems, where we are given a set of elements such that we can divide them into two parts. We are interested in knowing the smallest element in one part and the biggest element in the other part. The Two Heaps pattern is an efficient approach to solve such problems.

Time Complexity : O(log N)

## Why use it?
- find median of items in a stream
- need to know middle of list

## Concepts
- Need two heaps : minHeap & maxHeap
- if maxHeap - store and retrieve number in negative, so BIGGEST number is SMALLEST

## Complexity - Generally
- insert/ delete to head: O(log N ) - to push all is O(N log N)
- access root : O(1)
- Two heaps time complexity O(N log N) + O(N log N) => O(N log N)
- Space complexity => O(N) if we push both heaps - but can is aux of O(1)

## API
```
find_median(nums)
```

## How its done
### Choose Which heap to add element
```
if not self.maxHeap or -self.maxHeap[0] >= num:
    heappush(self.maxHeap, -num)
else:
    heappush(self.minHeap, num)
```
### Balance elements
```
# Either equal number in heaps or max-heap has one more
if len(self.maxHeap) > len(self.minHeap) + 1:
    heappush(self.minHeap, -heappop(self.maxHeap))
elif len(self.maxHeap) < len(self.minHeap):
    heappush(self.maxHeap, -heappop(self.minHeap))
```
### Find Median
```
if len(self.maxHeap) == len(self.minHeap):
    # we have even number of elements, take the average of middle two elements
    return -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0

# because max-heap will have one more element than the min-heap
return -self.maxHeap[0] / 1.0
```