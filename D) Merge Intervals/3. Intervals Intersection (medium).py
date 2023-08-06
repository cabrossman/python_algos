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


def merge(intervalsA, intervalsB):
  merged = []
  a,b = 0,0
  while b < len(intervalsB) and a < len(intervalsA):
    #no overlap
    if intervalsA[a].end < intervalsB[b].start or intervalsB[b].end < intervalsA[a].start:
      pass
    else:
      start = max(intervalsA[a].start, intervalsB[b].start)
      end = min(intervalsA[a].end, intervalsB[b].end)
      merged.append(Interval([start,end])) #intersection is smallest between two
    if intervalsB[b].end == intervalsA[a].end:
      a = a + 1
      b = b + 1
    elif intervalsB[b].end < intervalsA[a].end:
      b = b + 1
    else: # A.end is smaller
      a = a + 1
  return interval_to_list(merged)

B = list_to_interval([[1, 3], [5, 6], [7, 9]])
A = list_to_interval([[2, 3], [5, 7]])
assert merge(A, B) == [[2, 3], [5, 6], [7, 7]]

B = list_to_interval([[1, 3], [5, 7], [9, 12]])
A = list_to_interval([[5, 10]])
assert merge(A, B) == [[5, 7], [9, 10]]


print('all tests past!')