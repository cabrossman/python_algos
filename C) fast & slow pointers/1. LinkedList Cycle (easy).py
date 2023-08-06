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


def has_cycle(head, return_node = False):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            if return_node:
                return True, slow
            return True
    if return_node:
        return False, slow
    return False


def cycle_length(head):
    cycle_bool, slow = has_cycle(head, True)
    if not cycle_bool:
        return cnt
    cnt = 1
    fixed = slow
    slow = slow.next
    while fixed != slow and slow:
        slow = slow.next
        cnt = cnt + 1
    return cnt

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    assert has_cycle(head) == False

    #add cycle
    head.next.next.next.next.next.next = head.next.next
    assert has_cycle(head) == True

    # Mutate Cycle
    head.next.next.next.next.next.next = head.next.next.next
    assert has_cycle(head) == True
    assert cycle_length(head) == 3