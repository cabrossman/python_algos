"""
Given an array of K sorted LinkedLists, merge them into one sorted list.

Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]

"""

from heapq import heappush, heappop


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minHeap = []
    # put the root of each list in the min heap
    for root in lists:
        if root:
            heappush(minHeap, root)

    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    resultHead, resultTail = None, None
    while minHeap:
        node = heappop(minHeap)
        if resultHead is None:
            resultHead = resultTail = node  #start the new list
        else:
            resultTail.next = node          #connect the list
            resultTail = resultTail.next    #increment current node

        if node.next:
            heappush(minHeap, node.next)

    return resultHead

def format_output(node):
    l = []
    while node:
        l.append(node.value)
        node = node.next
    return l


l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4)

result = merge_lists([l1, l2, l3])
result = format_output(result)
assert result == [1, 2, 3, 3, 4, 6, 6, 7, 8]


l1 = ListNode(5)
l1.next = ListNode(8)
l1.next.next = ListNode(9)

l2 = ListNode(1)
l2.next = ListNode(7)

result = merge_lists([l1, l2])
result = format_output(result)
assert result == [1, 5, 7, 8, 9]

print('all tests have passed!')