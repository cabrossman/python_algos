def interval_intersection(A, B):
    #sort two lists
    A.sort(key = lambda x: x[0])
    B.sort(key = lambda x: x[0])
    result = []
    start, end = 0 , 1
    a, b = 0, 0
    while a < len(A) and b < len(B):
        #check for overlap
        if A[a][end] < B[b][start] or B[b][end] < A[a][start]:
            pass
        else: #if overlap create new var that is max of the start and min of ends
            i_start = max(A[a][start], B[b][start])
            i_end = min(A[a][end],B[b][end])
            result.append([i_start,i_end])
        #increment - smaller end int gets incremented end
        if A[a][end] < B[b][end]:
            a += 1
        elif A[a][end] > B[b][end]:
            b += 1
        # if same increment both
        else:
            a += 1
            b += 1
    return result

l1 = [[2, 6], [7, 9], [10, 13], [14, 19], [20, 24]]
l2 = [[1, 4], [6, 8], [15, 18]]
assert interval_intersection(l1,l2) == [[2, 4], [6, 6], [7, 8], [15, 18]]
l1 = [[1, 29]]
l2 = [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]
assert interval_intersection(l1,l2) == [[1, 5], [6, 10], [11, 14], [15, 18], [19, 20]]
print('all tests passed!')