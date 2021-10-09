"""
Given the head of a Singly LinkedList, write a method to modify the LinkedList 
such that the nodes from the second half of the LinkedList are inserted 
alternately to the nodes from the first half in reverse order. 
So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, 
your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

Your algorithm should not use any extra space 
and the input LinkedList should be modified in-place.

Input: [2, 4, 6, 8, 10, 12, None]
Output: [2, 12, 4, 10, 6, 8, None]

Input: [2, 4, 6, 8, 10, None]
Output: [2, 10, 4, 8, 6, None]

"""
import copy

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def summarize(self):
        l = []
        tail = self
        while tail:
            l.append(tail.value)
            tail = tail.next
        l.append(None)
        #print(l)
        return l



def create_linked_list(lst):
    #create linked list
    lst.pop()
    if len(lst) < 2:
        return Node(lst[0])
    head = Node(lst[0])
    tail = Node(lst[1])
    head.next = tail
    for i in lst[2:]:
        tail.next = Node(i)
        tail = tail.next
    tail.next = None
    _ = head.summarize()
    return head

def reverse(node):
  prev = None
  cnt = 0
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = next
    cnt = cnt + 1
  _ = prev.summarize()
  return prev, cnt

def insert_node(prev_node, new_node):
    # 1. check if the given prev_node exists
    if prev_node is None:
        raise Exception("List is empty")
    # 2. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
    # 3. make next of prev_node as new_node
    prev_node.next = new_node
    

def reorder(head):
    rtail, ll_len = reverse(copy.deepcopy(head))
    c2 = 1
    tail = head
    while ll_len > c2:
        #print(tail.value)


        # swap lists
        tmp = tail.next
        tail.next = rtail
        rtail = tmp
        tail = tail.next

        # inc counters
        c2 = c2 + 1
    #print(tail.value)
    tail.next = None

    return head.summarize()
    
        

if __name__ == "__main__":
    ll = create_linked_list([2, 4, 6, 8, 10, 12, None])
    assert reorder(ll) == [2, 12, 4, 10, 6, 8, None]
    ll = create_linked_list([2, 4, 6, 8, 10, None])
    assert reorder(ll) == [2, 10, 4, 8, 6, None]

    print("all tests have past")