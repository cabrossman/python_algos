
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    m1, end = head, head
    while end and end.next: #slow & fast pointer puts m1 in middle
        end = end.next.next
        m1 = m1.next

    cur = m1
    cur = cur.next
    prev = m1
    while cur: #reverse second half of list
        cur.next, prev, cur = prev, cur, cur.next
    
    #come inward checking. even number lists wont ever be palendromes
    tail = prev
    while head != tail: 
        if head.val != tail.val:
            return False
        if head == m1 or tail == m1:
            return False
        head = head.next
        tail = tail.next
    return True


# Creating the linked list that spells "racecar"
r = ListNode('r')
a1 = ListNode('a')
c1 = ListNode('c')
e = ListNode('e')
c2 = ListNode('c')
a2 = ListNode('a')
r2 = ListNode('r')

r.next = a1
a1.next = c1
c1.next = e
e.next = c2
c2.next = a2
a2.next = r2
assert is_palindrome(r) == True

# Creating the linked list that spells "raceecar"
r = ListNode('r')
a1 = ListNode('a')
c1 = ListNode('c')
e1 = ListNode('e')
e2 = ListNode('e')
c2 = ListNode('c')
a2 = ListNode('a')
r2 = ListNode('r')

r.next = a1
a1.next = c1
c1.next = e1
e1.next = e2
e2.next = c2
c2.next = a2
a2.next = r2
assert is_palindrome(r) == False
print('all tests have passed!')