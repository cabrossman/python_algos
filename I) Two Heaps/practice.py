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
  minheap = []
  maxheap = []

  def insert_num(self,num):
    #check if maxheap is empty - add
    if len(self.maxheap) == 0:
      heappush(self.maxheap, -num)
    #check if maxheap's head >= num - add (so it takes smaller numbers)
    elif -self.maxheap[0] >= num:
      heappush(self.maxheap, -num)
    # otherwise push to minheap
    else:
      heappush(self.minheap, num)

    #check to see if we need to rebaalance heaps
    # min heap should have higher numbers pointing to smallest
    # max heap should have smaller numbers pointing to biggest
    # maxheap should contain minheap + 1 as acceptable -> if not push to minheap
    # minheap shouldnt have more than maxheap -> if not push to maxheap

    if len(self.maxheap) > len(self.minheap) +1:
      tmp_num = -heappop(self.maxheap)
      heappush(self.minheap, tmp_num)
    elif len(self.maxheap) < len(self.minheap):
      tmp_num = heappop(self.minheap)
      heappush(self.maxheap, -tmp_num)

  def find_median(self):
    #if len of both heaps are equal average heads as median
    if len(self.maxheap) == len(self.minheap):
      return (-self.maxheap[0] + self.minheap[0]) / 2.0
    else:
      #otherwise - assume maxheap has one more element and that will be median
      return -self.maxheap[0]


medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
assert medianOfAStream.find_median() == 2.0
medianOfAStream.insert_num(5)
assert medianOfAStream.find_median() == 3.0
medianOfAStream.insert_num(4)
assert medianOfAStream.find_median() == 3.5
print('all tests pass!')