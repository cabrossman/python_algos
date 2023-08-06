def insert_interval(ints, insert_int):
    #start with variables
    ints.sort(key=lambda x: x[0])
    result = []
    A = insert_int
    start, end = 0, 1
    i = 0
    #add all before A
    while ints[i][end] < A[start] and i < len(ints):
        result.append(ints[i])
        i += 1
    #mutate A while overlap
    while not(A[end] < ints[i][start] or ints[i][end] < A[start]) and i < len(ints):
        A[start] = min(A[start], ints[i][start])
        A[end] = max(A[end], ints[i][end])
        i += 1
    #add A
    result.append(A)
    #add all those after A
    for j in range(i,len(ints)):
        result.append(ints[j])
    
    return result


assert insert_interval([[1,3], [5,7], [8,9], [10,13]], [2,6]) == [[1,7], [8,9],[10,13]]
assert insert_interval([[1,3], [6,9]], [2,5]) == [[1,5], [6,9]]
print('all tests passed!')