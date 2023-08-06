# 1. Sliding Window

## What is it?
Given an array, find the average/sum of all contiguous subarrays of size K in it. Could be variable window size

## Why use it?
- Given an array of positive numbers and a positive number S,find the length of the smallest contiguous subarray whose sum is greater than or equal to S. Return 0 if no such subarray exists.
- Given a string, find the length of the longest substring in it with no more than K distinct characters.

## Concepts
- **Sliding Window** : Calulate the sum of the previous subarray. To slide window forward subtract element going out from sum and add element comming in. It reduces the time from O(N*K) to O(N)

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

# 3. Fast and Slow Pointers

## What is it?

The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

Time Complexity : O(N)

## Why use it?
- Define if there is a cycle
- Return Length of cycle
- Find Start of Cycle
- Middle Node of Linked List
- Pallendrom Linked List

## Concepts
- Linked List Node
  ```
  class Node:
    def __init__(self, value, next=None):
      self.value = value
      self.next = next
  ```
## API
```
main(head)
```

## How its done
### LinkedList Cycle Tasks
1. Determine if Cycle (Fast and Slow Pointer - while fast and fast.next)
2. Find Cycle Length (fixed pointer and incremental pointer - while fixed != slow and slow)
3. Enter Cycle - (p1,p2 = head; while cycle_length > 0: p2 increment - will put p2 in cycle)
4. Find start of cycle (while p1 != p2 ; increment both p1 & p2)
```
def find_cycle_start(head):
  # determine cycle
  cycle_exist = False
  slow, fast = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      cycle_exist = True
      break #cycle found

  #find cycle length
  if not cycle_exist: 
    return -1
  cycle_length = 1
  fixed = slow
  slow = slow.next
  while fixed != slow and slow:
    cycle_length = cycle_length + 1
    slow = slow.next

  #Enter Cycle
  p1, p2 = head, head
  while cycle_length > 0:
    p2 = p2.next
    cycle_length = cycle_length - 1

  #find start of cycle
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next

  return p1
```
### Middle of LInked List
```
  def find_middle_of_linked_list(head):
      slow, fast = head, head
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
      return slow.value
```

# 4. Merge Intervals

## What is it?
This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Time Complexity : O(N*log(N)) for sorting & O(N) for merging intervals

## Why use it?
- Merge Intervals
- Insert Intervals
- Given two lists of intervals, find the intersection of these two lists. 
- Given an array of intervals representing 'N' appointments, find out if a person can attend all the appointments.


## Concepts
1. First Sort the intervals
2. Ways define overlap
    ```
    Given two intervals ('a' and 'b'), there will be six different ways the two intervals can relate to each other:
    1. They dont overlap, A ends before B starts
    2. They overlap. A occurs before. B ends after A
    3. A completely overlaps B
    4. They overlap. B occurs before. A ends after B.
    5. B completely overlaps A
    6. They dont overlap, B ends before A starts
    ```
3. Another way to say overlap
  ```
      NOT OVERLAP
      1. Aend < Bstart
      2. Bend < Astart

      OVERLAP
      1. Aend <= Bstart and Astart <= Bstart #B starts a bit later than A
      2. Bstart >= Astart & Bend <= Aend #B inside A
      3. Bend <= Astart and Bstart <= Astart #A starts a bit later than B
      4. Astart >= Bstart & Aend <= Bend #A inside B
  ```

## API
```
merge(intervals) #to merge itself
merge(intervalsA, intervalsB) # to merge two lists
```

## How its done
### Basic Algo to merge existing interavals together
Always remember to sort the interval based on START
```
def merge(intervals):
  merged = []
  intervals.sort(key = lambda x: x[0])
  if len(intervals) < 2:
      return intervals
  Astart, Aend = intervals.pop(0)
  for Bstart, Bend in intervals:
      if Bstart <= Aend: #overlap, extend the end
         Aend = max(Aend,Bend) 
      else: #some overlap
        merged.append([Astart, Aend])
        Astart, Aend = Bstart, Bend
  merged.append([Astart, Aend])
  return merged
```
### Insert Interval - find intersection
1. Loop while counters are less then interval len
2. If overlap - take max of start and min of end and append to merged list
3. Increment counters - if B.end < A.end Inc b else Inc A
```
def merge(intervalsA, intervalsB):
  merged = []
  a,b = 0,0
  while b < len(intervalsB) and a < len(intervalsA):
    #no overlap
    if intervalsA[a].end < intervalsB[b].start or intervalsB[b].end < intervalsA[a].start:
      pass
    else:
      start = max(intervalsA[a].start, intervalsB[b].start)
      end = min(intervalsA[a].end, intervalsB[b].end)
      merged.append(Interval([start,end]))
  
    if intervalsB[b].end == intervalsA[a].end:
      a = a + 1
      b = b + 1
    elif intervalsB[b].end < intervalsA[a].end:
      b = b + 1
    else: # A.end is smaller
      a = a + 1
  return interval_to_list(merged)
```

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

# 6. In-place Reversal of Linked List

## What is it?
We are asked to reverse the links between a set of nodes of a LinkedList. Often, the constraint is that we need to do this in-place, i.e., using the existing node objects and without using extra memory.

Time Complexity = O(N)

## Why use it?
- Reverse Linked List in Place
- Reverse Part of Linked List in Place
- Alternate two values of different linked lists

## Concepts
- Node
    ```
    class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    ```
- Increment Linked List
    ```
    current = current.next
    ```

## API
```
reverse(head) # reverse whole list
reverse(head, p, q) #reverse sublist
```

## How its done
### Basic Algo to sort linked list in place
```
def reverse(head):
    current, previous, next = head, None, None
    while current:
        next = current.next #store next value of orig list
        current.next = previous #make next value node point to last value
        previous = current # set previous head to current node
        current = next #increment current list
    return previous

```
### Reverse Sub Linked List
0. Initailize current = Head & previous = None
1. increment previous up to p-1 and current to p
2. Save current & previous - to hook up later
3. Swap but ensure you dont go more then q
4. Rreconnect - pont previous head to previous : p_previous.next = previous
5. p_current.next = current 
```
def reverse_sub_list(head, p, q):
  if p == q:
    return head
  current, previous = head, None
  i = 0
  # increment previous up to p-1 and current to p
  while current and i < p -1:
    previous = current
    current = current.next
    i = i + 1
  
  # save these to hook up later
  p_previous = previous
  p_current = current

  # swap current values with previous values
  # previous is always the head when we swap with current
  nxt = None
  i = 0
  while current and i < q - p + 1:
    nxt = current.next
    current.next = previous
    previous = current
    current = nxt
    i = i + 1
  
  if p_previous:
    #reconnect - pont previous head to previous
    p_previous.next = previous
  else:
    #otherwise previous was equal to head 
    head = previous

  #make end of list to hook back up incremented current
  p_current.next = current 

  #because everything was referencing pointers we mutated the ll
  # and we return the head
  return head
  ```

# 7. Breadth First Search

## What is it?
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level. 

Time Complexity : O(N)

## Why use it?
- Show levels top to bottom
- Show levels bottom to top
- Invert Binary Tree


## Concepts
- Tree Node
    ```
    class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    ```
- 3 Queues
    1. Queue (Q) - LIFO : always append(Nodes), pop(0)
    2. Current Level (CL) - node = Q.pop(0). CL.append(node) shows left to right, CL.appendleft(node) shows right to left
    1. Result (R) - R.append(CL) shows tree top to bottom, R.appendleft(CL) shows bottom to top
- Iteration
    ```
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):

            ...
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    ```



## API
```
traverse(root)
```

## How its done
### Show Levels Top to Bottom

```
result, queue = [], deque()
if not root:
    return result
queue.append(root)
while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
        currentNode = queue.popleft()
        currentLevel.append(currentNode.val)
        if currentNode.left: #add children
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    result.append(currentLevel)
return result
```
### Show Levels Bottom to Top
Just change this line from above
```
result.appendleft(currentLevel) #just append left
```
### Mutate Linked List
```
def connect_level_order_siblings(root):
  queue = deque()
  queue.append(root)
  while queue:
    previous = None
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        if previous:
            previous.next = node
        previous = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
  return
```

# 8. Depth First Search

## What is it?
Depth First Search (DFS) technique to traverse a tree.
We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.

Time Complexity : O(N^2)

## Why use it?
- Binary Tree Path Sum
- All Paths for a Sum
- A sum of Path Numbers
- A path with given sequence
- Count Paths for a Sum
- Tree Diameter

## Concepts
- Tree Node
    ```
    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    ```
- Recursion
    0. Pass external list to outside function to append to
    1. Handle Edge cases & Terminal Case
    2. Handle path for `left` and path for `right`
    3. To keep state pass a named list into the head of recursive function
    4. IF a SUM subtract values on recursive calls
    5. No work is done until leaf nodes and we pop up the stack. 

- Breadth First Search
    1. Go deepest to terminal node and then go wide

## API
```
traverse(root)
```

## How its done
### Binary Tree Path Sum
```
def has_path(root, _sum):
  if not root:
    return False
  if (
        root.val == _sum  
        and not root.left 
        and not root.right
    ): # terminal path
        return True
  return has_path(root.left, _sum - root.val) or has_path(root.right, _sum - root.val)
```
### All Paths for a Sum
```
    if currentNode is None:
        return

    # add the current node to the path
    current_path.append(currentNode.val)

    # terminal path
    if (
        currentNode.val == _sum 
        and not currentNode.left 
        and not currentNode.right
    ):
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(
            currentNode = currentNode.left, 
            _sum = _sum - currentNode.val, 
            current_path = current_path,
            all_paths = all_paths
        )
        # traverse the right sub-tree
        find_paths_recursive(
            currentNode = currentNode.right, 
            _sum = _sum - currentNode.val, 
            current_path = current_path,
            all_paths = all_paths
        )
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]
```
### Path with a given sequence
```
if not root:
    return False
current_seq.append(root.val)
if current_seq == sequence:
    return True
else:
    left = find_path(root = root.left,sequence = sequence,current_seq = current_seq)
    right = find_path(root = root.right,sequence = sequence, current_seq = current_seq)
del current_seq[-1]
return left or right
```
### Count the Sum of Paths. 
Make sure to sum the paths at a terminal node
```
if (not node.left and not node.right):
    tot = 0
    for val in current_path[::-1]: #iterate backwards (or pop)
        tot = tot + val
        if tot == _sum:
            all_paths.append(list(current_path))
```

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

# 10. Subsets

## What is it?
Permutations and Combinations of a given set of elements. This pattern describes an efficient Breadth First Search (BFS) approach to handle all these problems.

time complexity : O(N * 2^N)

## Why use it?
- Subsets, All distinct elements (list of sets) event lists with dups
- Permutations & string permutations (w/case)

## Concepts
- Breadth First Search
- If given duplicates sort first
- each iteration (with a new number) doubles the prior by adding a new combination.
- Algo is add empty set. append previous sets and new number to double sets. Repeat
- If duplicate skip up to unique parts
- for permutations add last number to all positions


## API
```
find_subsets(nums)
```

## How its done
### Distinct Subsets
```
def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    for i in range(len(subsets)):
      subset = list(subsets[i])
      subset.append(num)
      subsets.append(subset)
  return subsets
```

## Variants
### Duplicates
```
def find_subsets(nums):
  nums.sort()
  subsets = [[]]
  start, end = 0,0
  for i in range(len(nums)):
    start = 0
    if i > 0 and nums[i] == nums[i-1]:
      start = end
    end = len(subsets)
    for j in range(start, end):
      subset = list(subsets[j])
      subset.append(nums[i])
      subsets.append(subset)
  return subsets
```
### Permutations
```
def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])
    for i in range(len(nums)): # on the last iteration everything is added to result
        for _ in range(len(permutations)): #later we add to permutation
            # we pop to mutate the list in the deque
            permutation_A = permutations.popleft() #this saves the n-1 version to add to list later
            #need one more than n which only has 2 in the example to get all permutations
            for j in range(len(permutation_A) + 1): 
                permutation_B = list(permutation_A)
                permutation_B.insert(j, nums[i]) #we insert the nth number at each possible position
                if len(permutation_B) == len(nums): ### must have all numbers and add to result
                    result.append(permutation_B)
                else:
                    permutations.append(permutation_B) ###intermediatery
    return result

```

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

# 12. Bitwise XOR

## What is it?
XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise.

## Why use it?
- Find missing number from array of non sorted integers. Doing so in the classical way can result in integer overflow, but XOR works without problem
- Find which number doesnt appear twice

## Concepts
### Taking XOR of a number with itself returns 0, e.g.,
```
1 ^ 1 = 0
29 ^ 29 = 0
```

### Taking XOR of a number with 0 returns the same number, e.g.,
```
1 ^ 0 = 1
31 ^ 0 = 31
```

### XOR is Associative & Commutative, which means:
```
(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
```

### Other Concepts
```
number ^ complement = all_bits_set
number ^ number ^ complement = number ^ all_bits_set
0 ^ complement = number ^ all_bits_set
complement = number ^ all_bits_set
```
## API
```
main(arr)
```

## How its done
### 1. Find missing Number
1. XOR all number from 1 to n - call this x1
2. XOR all the numbers in input array - call this x2
3. x1 ^ x2
```
def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2
```

### 2. Find single number in list of duplicates
```
from functools import reduce
reduce(lambda x, y: x ^ y, arr)
```

### 3. Other Variants
1. "#2" - Two numbers arent doubled example
2. Return compliment in base 10

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

# 15. Knapsack

## What is it?
0/1 Knapsack pattern is based on the famous problem with the same name which is efficiently solved using Dynamic Programming (DP).

Time Complexity of KnapSack = O(N * C)

## Why use it?
- Knapsack problem
- Equal Subset Sum (split list into two subsets and find equal sums)
- Overlapping sets

## Concepts
- DP = dynamic programming
- List of Lists

## API
```
solve_knapsack(profits, weights, capacity)
```

## How its done (all examples)
### 1. Setup and handle edge case
```
  ROWS = len(profits)
  COLUMNS = capacity + 1
  if len(profits) != len(weights) or capacity < 1:
    return 0
```
### 2. Create DP & set default (0 or False)
```
  dp = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
```
### 3. Mutate Defaults - for Knapsack we take all where capacity >= Weights in first row
```
  for c in range(COLUMNS):
    if c >= weights[0]:
      dp[0][c] = profits[0]
```
### 4. Iterate over all elements of DP. "Take" item if you have enough capacity and its higher than not taking item. Remember this for next iteration
```
  for i in range(1, ROWS): #0th row already iterated.
    for c in range(1, COLUMNS): #0th column has 0 capacity
      profit1, profit2 = 0, 0
      if c >= weights[i]:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      profit2 = dp[i - 1][c]

      dp[i][c] = max(profit1, profit2)
```
### 5. Return bottom right
```
return dp[ROWS-1][COLUMNS-1]
```

# 16. Topological Sort

## What is it?
Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if task B is dependent on task A, A comes before B in topological ordering.

time complexity = O(V + E)

## Why use it?
- If asked Topological Sort
- If asked the order of tasks given dependancies

## Concepts
Here are a few fundamental concepts related to topological sort:
- **Source**: Any node that has no incoming edge and has only outgoing edges is called a source.
- **Sink**: Any node that has only incoming edges and no outgoing edge is called a sink.

Topological ordering starts with one of the sources and ends at one of the sinks.

`A topological ordering is possible only when the graph has no directed cycles`

## API
```
topological_sort(vertices, edges)
```

## How its done (all examples)
### 1. Handle edge case
```
  if vertices <= 0:
    return []
```
### 2. Initialize the Graph
```
inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
graph = {i: [] for i in range(vertices)}  # adjacency list graph
```
### 3. Build the graph
```
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree
```
### 4. Find all sources (those with 0 inDegree)
```
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)
```
### 5. Find Topological Order
```
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)
```

# 17. Excel Solve

## What is it?
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
Given an column title, return its corresponding integer columnNumber as it appears in an Excel sheet.

## Concepts
Python `ord()` function returns the Unicode code integer from a given character.
- `ord('A') == 65`
- `ord('Z') == 90`
Python `chr()` function returns the Unicode character from a given integer
- `chr(65) == A`
- `chr(24 + ord('A')) == 'Y'`

Python `%` returns the integer remainder when taking a larger number into a smaller 
-  `26**3 % 26 == 0`
- `9 % 5 == 4`


Let's see the relationship between the Excel sheet column title and the number:
A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26

Now we can see that ABCD＝A×26³＋B×26²＋C×26¹＋D＝1×26³＋2×26²＋3×26¹＋4

But how to get the column title from the number? We can't simply use the n%26 method because:

ZZZZ＝Z×26³＋Z×26²＋Z×26¹＋Z＝26×26³＋26×26²＋26×26¹＋26

We can use (n-1)%26 instead, then we get a number range from 0 to 25.

## How its done
### Num to Char
```
def convertToTitle(num):
    caps = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    result = []
    while num > 0:
        last_char_int = (num -1) % 26
        last_char = caps[last_char_int]
        result.append(last_char)
        num = (num -1) // 26
    result.reverse()
    return ''.join(result)
```

### Chr to Num
The while statement allows a flexible window size. It shrinks the window start
```
def convertToInt(COLS):
    tot = 0
    for i, col in enumerate(COLS[::-1]):
        char_int = ord(col) - ord('A') + 1
        subtotal = char_int*(26**i)
        tot = tot + subtotal
    return tot
```