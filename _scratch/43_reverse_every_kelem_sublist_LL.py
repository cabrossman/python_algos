
"""
Given the head of a LinkedList and a number k, 
reverse every k sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than k elements, 
reverse it too.
"""

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
    
def reverse_every_k_elements(head, k):
    if k <= 1:
        return head
    curr, prev = head, None
    while curr:
        i, nxt = 0, None
        p_prev, p_curr = prev, curr
        while curr and i < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            i += 1
        if p_prev:
            p_prev.next = prev
        else:
            head = prev
        p_curr.next = curr
        prev = p_curr
    return head
       

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_every_k_elements(head, 3)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()
