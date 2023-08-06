"""
There are a total of n classes labeled with 
the English alphabet (A, B, C, and so on). 
Some classes are dependent on other classes for compilation. 
For example, if class B extends class A, then B has a dependency on A. 
Therefore, A must be compiled before B.

Given a list of the dependency pairs, 
find the order in which the classes should be compiled.
"""

from collections import deque

def find_compilation_order(edges):
    lst, graph, in_degree = [], {}, {}
    if not edges:
        return lst
  
    #build graph
    for edge in edges:
        [child, parent] = edge
        if parent not in graph:
            graph[parent] = []
            graph[parent].append(child)
        else:
            graph[parent].append(child)
        in_degree[child] = in_degree.get(child,0) + 1

    source = deque()
    for vert, ins in in_degree.items():
        if ins == 0:
            source.append(vert)

    while source:
        vert = source.popleft()
        lst.append(vert)
        for child in graph[vert]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)
    
    return lst

find_compilation_order([['A', 'B'], ['B', 'C'], ['A', 'D']]) == ['C','B','D','A']
find_compilation_order([['A', 'B'], ['B', 'C'], ['C', 'D']]) == ['D', 'C', 'B', 'A']
print('all tests passed!')