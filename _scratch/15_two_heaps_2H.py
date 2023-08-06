"""
Design a class to calculate the median of a number stream. 
The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, 
the median will be the average of the middle two numbers.

"""
from heapq import *


class MedianOfAStream:

  maxHeap = []  # containing first half of numbers
  minHeap = []  # containing second half of numbers

  def insert_num(self, num):
    #push in max heap if its none OR num < max_heap head
    #else minheap
    if not self.maxHeap:
      heappush(self.maxHeap, -num)
    elif num < -self.maxHeap[0]:
      heappush(self.maxHeap, -num)
    else:
      heappush(self.minHeap, num)

    #rebalance
    #if max heap is smaller put there
    if len(self.minHeap) > len(self.maxHeap):
      tmp = heappop(self.minHeap)
      heappush(self.maxHeap, -tmp)
    #if min heap is smaller by 2 put in there
    elif len(self.maxHeap) - len(self.minHeap) >= 2:
      tmp = heappop(self.maxHeap)
      heappush(self.minHeap, -tmp)

  def find_median(self):
    #determine if odd or even
    tot = len(self.maxHeap) + len(self.minHeap)
    is_odd = (tot % 2 == 1)
    min_heap_top = self.minHeap[0]
    max_heap_top = self.maxHeap[0] * -1
    max_heap_longer = len(self.maxHeap) > len(self.minHeap)
    if is_odd and max_heap_longer:
      return max_heap_top
    elif is_odd:
      return min_heap_top
    else:
      return (min_heap_top + max_heap_top)/2.0


medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
assert medianOfAStream.find_median() == 2.0
medianOfAStream.insert_num(5)
assert medianOfAStream.find_median() == 3.0
medianOfAStream.insert_num(4)
assert medianOfAStream.find_median() == 3.5
print('all tests passed!')
