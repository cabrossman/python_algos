
The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.

One of the famous problems solved using this technique was Finding a cycle in a LinkedList. Let's jump onto this problem to understand the Fast & Slow pattern.


```
def has_cycle(head):
  slow, fast = head, head
  while fast and fast.next:
    fast = fast.next.next
    slow = slow.next
    if slow == fast:
      return True  # found the cycle
  return False
```

always save start of ll as head
increment always through next
```
# increment ll
tail = head
tail = tail.next
```

find middle of list
```
def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value
```

reverse
```
def reverse(node):
  prev = None
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = next
  return prev
```

swap list nodes
```
# swap lists
tmp = tail.next
tail.next = rtail
rtail = tmp
tail = tail.next
```