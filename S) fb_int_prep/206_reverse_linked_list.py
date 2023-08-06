"""
Reverse Linked List

"""

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def reverse_ll(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
one.next = two
two.next = three
three.next = four
four.next = five
cur = reverse_ll(one)
while cur:
    print(cur.val)
    cur = cur.next