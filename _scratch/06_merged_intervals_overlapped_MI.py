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
"""

def merge(intervals):
    merged = []
    intervals.sort(lambda x: x[0])
    Astart, Aend = intervals.pop(0)
    for Bstart, Bend in intervals:
        if Bstart <= Aend: #overlap
            Aend = max(Aend,Bend)
        else: #no overlap
            merged.append([Astart, Aend])
            Astart, Aend = Bstart, Bend #increment up
    merged.append([Astart, Aend])
    return merged

assert merge([[1,4], [2,5], [7,9]]) == [[1,5], [7,9]]
assert merge([[6,7], [2,4], [5,9]]) == [[2,4], [5,9]]
assert merge([[1,4], [2,6], [3,5]]) == [[1,6]]
