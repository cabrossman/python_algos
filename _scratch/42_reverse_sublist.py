
"""
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
"""
from copy import deepcopy

class Node:
  def __init__(self, value, next=None):
    self.val = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.val, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
    if p == q:
        return head

    curr, prev, nxt = head, None, None
    i = 0
    #increment curr up to p
    while curr and i < p -1:
        prev = curr
        curr = curr.next
        i += 1
    #pointers to hook up after reveresal
    pprev, pcurr = prev, curr
    
    #reverse in place - while i < range of p&q
    i = 0
    while curr and i <= (q - p):
       nxt = curr.next
       curr.next = prev
       prev = curr
       curr = nxt
       i += 1

    if pprev:
       pprev.next = prev
    else:
       head = prev
    
    pcurr.next = curr
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

