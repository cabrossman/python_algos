def merge_intervals(intervals):
    intervals.sort(key = lambda x: x[0])
    result = []
    A = intervals[0]
    start, end = 0, 1
    for B in intervals:
        if A[end] < B[start]: #no overlap
            result.append(A)
            A = B
        else:
            #only need to extend end since start is sorted
            A[end] = max(A[end], B[end])
    result.append(A)
    return result


assert merge_intervals([[1,4], [2,5], [7,9]]) == [[1,5], [7,9]]
assert merge_intervals([[6,7], [2,4], [5,9]]) == [[2,4], [5,9]]
assert merge_intervals([[1,4], [2,6], [3,5]]) == [[1,6]]
print('all tests passed!')