"""
Given an array of K sorted LinkedLists, merge them into one sorted list.

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]

"""

from heapq import heappush, heappop

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

    def __lt__(self,other):
        return self.val < other.val

def kth_smallest_kway(ll_lists, kth_smallest):
    min_heap = [] #returns smallest keeps largest

    #get first node in each list
    for ll in ll_lists:
        heappush(min_heap, ll)

    counter = 0
    while min_heap:
        node = heappop(min_heap)        
        if node.next:
            heappush(min_heap, node.next)
        counter = counter + 1
        if counter == kth_smallest:
            break
    
    return node.val

l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)
#[1, 2, 3, 3, 4, 6, 6, 7, 8]
result = kth_smallest_kway([l1, l2, l3], 5)
assert result == 4

result = kth_smallest_kway([l1, l2, l3], 7)
assert result == 6


l1 = ListNode(5)
l1.next = ListNode(8)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(7)

#[1, 5, 7, 8, 9]
result = kth_smallest_kway([l1, l2], 10)
assert result == 9

print('all tests have passed!')