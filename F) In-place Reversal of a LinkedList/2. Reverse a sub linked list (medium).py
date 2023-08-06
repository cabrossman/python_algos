
"""
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
"""
from copy import deepcopy

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


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


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_sub_list(head,2,4)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()