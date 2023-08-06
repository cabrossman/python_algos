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

## Complexity - Generally
- time complexity : O(N)
- space complexity : O(1)

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