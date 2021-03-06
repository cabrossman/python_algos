"""
    Topological Sort of a directed graph (a graph with unidirectional edges) 
    is a linear ordering of its vertices such that for every directed edge (U, V) 
    from vertex U to vertex V, U comes before V in the ordering.

    Given a directed graph, find the topological ordering of its vertices.

    Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
    Output: Following are the two valid topological sorts for the given graph:
    1) 3, 2, 0, 1
    2) 3, 2, 1, 0

    Input: Vertices=5, Edges=[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]
    Output: Following are all valid topological sorts for the given graph:
    1) 4, 2, 3, 0, 1
    2) 4, 3, 2, 0, 1
    3) 4, 3, 2, 1, 0
    4) 4, 2, 3, 1, 0
    5) 4, 2, 0, 3, 1

    Input: Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]
    Output: Following are all valid topological sorts for the given graph:
    1) 5, 6, 3, 4, 0, 1, 2
    2) 6, 5, 3, 4, 0, 1, 2
    3) 5, 6, 4, 3, 0, 2, 1
    4) 6, 5, 4, 3, 0, 1, 2
    5) 5, 6, 3, 4, 0, 2, 1
    6) 5, 6, 3, 4, 1, 2, 0

    There are other valid topological ordering of the graph too.
"""

from collections import deque


def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  # assumes atleast 1 vertex has no incomming degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder


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