# 14. K-Way Merge

## What is it?
This pattern helps us solve problems that involve a list of sorted arrays. Whenever we are given K sorted arrays, we can use a Heap to efficiently perform a sorted traversal of all the elements of all arrays.

Time Complexity : O(N * log K)


## Why use it?
- Linked Lists that need to be merged.
- When given K sorted array and need to merge them in a sorted order
- Find the "4th" smallest numbers amoung all K sorted arrays

## Concepts
- Min Heap. Data Structure that always points to smallest element.
- When creating custom objects we need a method `__lt__` to be able to compare eachother.
    ```
    class ListNode:
        def __init__(self, value):
            self.value = value
            self.next = None

        # used for the min-heap
        def __lt__(self, other):
            return self.value < other.value
    ```

## API
```
merge_lists(lists)
```

## How its done
### 1. Initialize Heap
We can push the smallest (first) element of each sorted array in a Min Heap to get the overall minimum. While inserting elements to the Min Heap we keep track of which array the element came from.
```
from heapq import heappush, heappop
minHeap = []
for root in lists:
    if root:
        heappush(minHeap, root)
```
### 2. Remove top element
Remove the top element from the heap to get the smallest element and push the next element from the same array to heap, to which this smallest element belonged, to the heap. Connect list along the way. Stop when no more elements in heap. 
```
resultHead, resultTail = None, None
while minHeap:
    node = heappop(minHeap)
    if resultHead is None:
        resultHead = resultTail = node  #start the new list
    else:
        resultTail.next = node          #connect the list
        resultTail = resultTail.next    #increment current node

    if node.next:
        heappush(minHeap, node.next)
return resultHead
```