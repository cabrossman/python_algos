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

## Complexity - Generally
time complexity : O(N)
space complexity : O(1) - doesnt store values

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