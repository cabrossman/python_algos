
from collections import deque


def topological_sort(vertices, edges):
    lst, graph, in_degree = [], {}, {}
    if vertices <= 0:
        return lst
    
    #build graphs and containers
    for i in range(vertices):
        graph[i] = [] #parent : child_list
        in_degree[i] = 0 #child : in_degrees
    sources = deque()

    #populate graph
    for edge in edges:
        [parent, child] = edge
        graph[parent].append(child)
        in_degree[child] += 1
    

    #add sources
    for child, ins in in_degree.items():
        if ins == 0:
            sources.append(child)

    #sort
    while sources:
        vert = sources.popleft()
        lst.append(vert)
        for child in graph[vert]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(lst) != vertices:
        return []
    
    return lst


assert topological_sort(4, [
    [3, 2], [3, 0], [2, 0], [2, 1]
]) == [3, 2, 0, 1]
assert topological_sort(5, [
    [4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
]) == [4, 2, 3, 0, 1]
assert topological_sort(7, [
    [6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
]) == [5, 6, 3, 4, 0, 2, 1]
print('all tests have passed!')