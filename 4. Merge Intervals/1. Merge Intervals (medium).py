"""
Given a list of intervals, 
merge all the overlapping intervals to produce a list 
that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
one [1,5].

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.

Sorting is O(N * log(N)), Merging O(N)
"""

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    return "[" + str(self.start) + ", " + str(self.end) + "]"


def merge(intervals):
  merged = []
  # sort intervals
  intervals.sort(key = lambda x: x.start)
  if len(intervals) < 2:
      return intervals
  for i, B in enumerate(intervals):
      if i == 0: #setup comparison on first loop
          A = B
          continue
      if B.start > A.end: #no overlap
          merged.append(A)
          A = B
      else: #some overlap
        min_start = min(B.start, A.start)
        max_end = max(B.end, A.end)
        A = Interval(min_start, max_end)
        merged.append(A)
  return merged

def main():
  print("Merged intervals: ")
  s=''
  for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    s = s + i.print_interval()
  print("[" + s + "]")

  print("Merged intervals: ")
  s=''
  for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    s = s + i.print_interval()
  print("[" + s + "]")

  print("Merged intervals: ")
  s=''
  for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    s = s + i.print_interval()
  print("[" + s + "]")

main()