"""
Given an array of intervals representing 'N' appointments, 
find out if a person can attend all the appointments.

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.


Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.


Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.

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


def can_attend_all_appointments(X):
  X.sort(key = lambda x: x.start)
  left = 0
  right = len(X) -1
  while left < right:
    #no overlap
    if not (X[left].end < X[right].start or X[left].end < X[right].start):
      return False
    if X[right].end >= X[left].end:
      right = right - 1
    else: 
      left = left + 1
  return True

X = list_to_interval([[1,4], [2,5], [7,9]])
assert can_attend_all_appointments(X) == False

X = list_to_interval([[6,7], [2,4], [8,12]])
assert can_attend_all_appointments(X) == True

X = list_to_interval([[4,5], [2,3], [3,6]])
assert can_attend_all_appointments(X) == False


print('all tests past!')