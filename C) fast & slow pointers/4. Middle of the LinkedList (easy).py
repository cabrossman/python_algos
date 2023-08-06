"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4
"""
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def create_linked_list(tail_val):
    #create linked list
    if tail_val <= 2:
        return 1
    head, tail = Node(1), Node(2)
    head.next = tail
    for i in range(3, tail_val+1):
        tail.next = Node(i)
        tail = tail.next
    tail.next = None
    return head

def find_middle_of_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

if __name__ == "__main__":
    ll = create_linked_list(3)
    assert find_middle_of_linked_list(ll) == 2
    ll = create_linked_list(5)
    assert find_middle_of_linked_list(ll) == 3
    ll = create_linked_list(6)
    assert find_middle_of_linked_list(ll) == 4
    ll = create_linked_list(7)
    assert find_middle_of_linked_list(ll) == 4

    print("all tests have past")