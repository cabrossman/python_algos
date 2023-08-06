"""
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.

O(N)
"""
from __future__ import print_function
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

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

  #find start of cycle
  p1, p2 = head, head
  while cycle_length > 0:
    p2 = p2.next
    cycle_length = cycle_length - 1

  #find start of cycle
  while p1 != p2:
    p1 = p1.next
    p2 = p2.next

  return p1

if __name__ == "__main__":
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  assert find_cycle_start(head).value == 3

  head.next.next.next.next.next.next = head.next.next.next
  assert find_cycle_start(head).value == 4

  head.next.next.next.next.next.next = head
  assert find_cycle_start(head).value == 1

  head.next.next.next.next.next.next = head.next.next.next.next.next
  assert find_cycle_start(head).value == 6

  print("all tests have past")