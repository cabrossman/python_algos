"""
Given the head of a Singly LinkedList, 
write a function to determine if the LinkedList has a cycle in it or not.

head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 3 = True
head -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> Null = False

O(N)
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True, slow
    return False, None


def cycle_length(head):
    curr = head
    cycle, node = has_cycle(head)
    if not cycle:
       return 0
    i = 0
    while node != curr:
       curr = curr.next
       i += 1
    return i

def find_cycle_start(head):
    cyc_len = cycle_length(head)
    p1 = p2 = head
    for _ in range(cyc_len):
       p1 = p1.next

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
    has, node = has_cycle(head)
    assert has == False

    #add cycle
    head.next.next.next.next.next.next = head.next.next
    has, node = has_cycle(head)
    assert has == True

    # Mutate Cycle
    head.next.next.next.next.next.next = head.next.next.next
    has, node = has_cycle(head)
    assert has == True
    assert cycle_length(head) == 3
    print('all tests passed!')



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