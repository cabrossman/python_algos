"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all 
necessary intervals to produce a list that has only mutually exclusive intervals.

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
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


def insert_interval(intervals, new_interval):
  merged = []
  intervals.sort(key = lambda x: x.start)
  i = 0
  # Add all with no overlap before A
  while i < len(intervals) and intervals[i].end < new_interval.start:
    merged.append(intervals[i])
    i = i + 1

  #mutate A with all those with overlap
  while i < len(intervals) and intervals[i].start <= new_interval.end:
    new_interval.end = max(new_interval.end, intervals[i].end)
    new_interval.start = min(new_interval.start, intervals[i].start)
    i = i + 1

  #Add New A
  merged.append(new_interval)

  #Add all without overlap after A
  while i < len(intervals):
    merged.append(intervals[i])
    i = i + 1
  
  return interval_to_list(merged)

interval_list = list_to_interval([[1,3], [5,7], [8,12]])
to_insert = Interval([4,6])
assert insert_interval(interval_list, to_insert) == [[1,3], [4,7], [8,12]]

interval_list = list_to_interval([[1,3], [5,7], [8,12]])
to_insert = Interval([4,10])
assert insert_interval(interval_list, to_insert) == [[1,3], [4,12]]

interval_list = list_to_interval([[2,3],[5,7]])
to_insert = Interval([1,4])
assert insert_interval(interval_list, to_insert) == [[1,4], [5,7]]
print('all tests past!')