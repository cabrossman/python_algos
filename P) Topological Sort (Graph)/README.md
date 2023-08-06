# 16. Topological Sort

## What is it?
Topological Sort is used to find a linear ordering of elements that have dependencies on each other. For example, if task B is dependent on task A, A comes before B in topological ordering.

time complexity = O(V + E)

## Why use it?
- If asked Topological Sort
- If asked the order of tasks given dependancies

## Concepts
Here are a few fundamental concepts related to topological sort:
- **Source**: Any node that has no incoming edge and has only outgoing edges is called a source.
- **Sink**: Any node that has only incoming edges and no outgoing edge is called a sink.

Topological ordering starts with one of the sources and ends at one of the sinks.

`A topological ordering is possible only when the graph has no directed cycles`

## Complexity
- Time Complexity: O(V+E)
- Space Complexity:Aux O(V)

## API
```
topological_sort(vertices, edges)
```

## How its done (all examples)
### 1. Handle edge case
```
  if vertices <= 0:
    return []
```
### 2. Initialize the Graph
```
inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
graph = {i: [] for i in range(vertices)}  # adjacency list graph
```
### 3. Build the graph
```
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree
```
### 4. Find all sources (those with 0 inDegree)
```
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)
```
### 5. Find Topological Order
```
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)
```