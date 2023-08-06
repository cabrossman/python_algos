from heapq import heappush, heappop

def merge(lists):
    min_heap = [] #returns smallest keeps largest
    result = []

    #create a map for keeping track of the list
    array_map ={f'l{i + 1}': l for i, l in enumerate(lists)}

    for list_id, lst in array_map.items():
        pointer = 0
        n = lst[pointer]
        tup = (n, pointer, list_id) #store number, pointer of list and list id
        heappush(min_heap, tup)

    while min_heap:
        (n, pointer, list_id) = heappop(min_heap)
        result.append(n)
        if pointer + 1 < len(array_map[list_id]): #check if next point in bounds
            n = array_map[list_id][pointer + 1] #access next elem
            pointer += 1 #inc pointer
            tup = (n, pointer, list_id) #store in heap
            heappush(min_heap, tup)
    
    return result


l1 = [2, 5, 8]
l2 = [1, 3, 6, 9]
l3 = [4, 5, 6, 7, 10]
result = merge([l1, l2, l3])
assert result == [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 10]
print('all tests have passed!')