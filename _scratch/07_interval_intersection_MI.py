"""
Given two lists of intervals, find the intersection of these two lists. 
Each list consists of disjoint intervals sorted on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.


NOT OVERLAP
1. Aend < Bstart
2. Bend < Astart

OVERLAP
1. Aend <= Bstart and Astart <= Bstart #B starts a bit later than A
2. Bstart >= Astart & Bend <= Aend #B inside A
3. Bend <= Astart and Bstart <= Astart #A starts a bit later than B
4. Astart >= Bstart & Aend <= Bend #A inside B
"""

class Interval:
  def __init__(self, values) -> None:
      s, e = values
      self.start = s
      self.end = e

def interval_to_list(interval_list):
  return [[i.start, i.end] for i in interval_list]

def list_to_interval(lst):
  interval_list = []
  for values in lst:
    interval_list.append(Interval(values))
  return interval_list


def merge(intA, intB):
  merged = []
  a,b = 0,0
  while a < len(intA) and b < len(intB):
    if intA[a].end < intB[b].start or intB[b].end < intA[a].start:
      pass # no overlap
    else:
      start = max(intB[b].start, intA[a].start) #largest start
      end = min(intB[b].end, intA[a].end) #smallest end
      merged.append(Interval([start,end]))
    if intA[a].end < intB[b].end:
      a += 1
    elif intA[a].end > intB[b].end:
      b += 1
    else:
      a += 1
      b += 1
  return interval_to_list(merged)

B = list_to_interval([[1, 3], [5, 6], [7, 9]])
A = list_to_interval([[2, 3], [5, 7]])
assert merge(A, B) == [[2, 3], [5, 6], [7, 7]]

B = list_to_interval([[1, 3], [5, 7], [9, 12]])
A = list_to_interval([[5, 10]])
assert merge(A, B) == [[5, 7], [9, 10]]


print('all tests past!')