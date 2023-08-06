
"""
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
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


def reverse(head):
    current, previous, next = head, None, None
    while current:
        next = current.next #store next value of orig list
        current.next = previous #make next value node point to last value
        previous = current # set previous head to current node
        current = next #increment current list
    return previous


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse(head)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()