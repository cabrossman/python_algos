"""
Given M sorted arrays, find the Kth smallest number among all the arrays.

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
Output: 4
Explanation: The 5th smallest number among all the arrays is 4, this can be verified from 
the merged list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Input: L1=[5, 8, 9], L2=[1, 7], K=3
Output: 7
Explanation: The 3rd smallest number among all the arrays is 7.

"""

from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def find_Kth_smallest(lists, K):
    minHeap = []

    # put the root of each list in the min heap
    for root in lists:
        if root:
            heappush(minHeap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    resultHead, resultTail = None, None
    cnt = 0
    while minHeap:
        node = heappop(minHeap)
        cnt = cnt + 1
        if cnt == K:
            return node.value
        if resultHead is None:
            resultHead = resultTail = node  #start the new list
        else:
            resultTail.next = node          #connect the list
            resultTail = resultTail.next    #increment current node

        if node.next:
            heappush(minHeap, node.next)

    return resultHead


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

assert find_Kth_smallest([l1, l2, l3], K=5) == 4


l1 = ListNode(5)
l1.next = ListNode(8)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(7)


assert find_Kth_smallest([l1, l2], K=3) == 7
print('all tests have passed!')