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
    
def reorder_list(head):
    if not head:
        return head
    
    curr = fast = head #get to middle of list
    while fast and fast.next:
        curr = curr.next
        fast = fast.next.next 
    
    prev = None #reverse second half of list
    while curr:
        curr.next, prev, curr = prev, curr, curr.next 

    first, second = head, prev #head = start of list, prev = end of list
    while second.next: #while end of list has next value
        first.next, first = second, first.next
        second.next, second = first, second.next
    
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
result = reorder_list(head)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()
