"""
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original 
form once the algorithm is finished. The algorithm should have O(N) time complexity where
'N' is the number of nodes in the LinkedList.

Input: [2,4,6,4,2]
Output: true

Input: [2,4,6,8,6,4,2]
Output: true

Input: [2,4,6,4,2,2]
Output: false

"""
import copy

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def create_linked_list(lst):
    #create linked list
    if len(lst) < 2:
        return Node(lst[0])
    head = Node(lst[0])
    tail = Node(lst[1])
    head.next = tail
    for i in lst[2:]:
        tail.next = Node(i)
        tail = tail.next
    tail.next = None
    return head

def reverse(node):
  prev = None
  while node:
    next = node.next
    node.next = prev
    prev = node
    node = next
  return prev


def is_palondrome(head):
    if not head or not head.next:
        return False

    # find middle of linked list
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Need Odd number of total eliments
    if fast is None:
        return False
    
    #slow = middle of list for pallendrome 
    head_second_half = reverse(copy.deepcopy(slow))  # reverse the second half

    while head and head_second_half:
        if head.value != head_second_half.value:
            return False
        head = head.next
        head_second_half = head_second_half.next

    return True

    
        

if __name__ == "__main__":
    ll = create_linked_list([2,4,6,4,2])
    assert is_palondrome(ll) == True
    ll = create_linked_list([2,4,6,8,6,4,2])
    assert is_palondrome(ll) == True
    ll = create_linked_list([2,4,6,4,2,2])
    assert is_palondrome(ll) == False

    print("all tests have past")