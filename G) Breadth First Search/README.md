# 7. Breadth First Search

## What is it?
This pattern is based on the Breadth First Search (BFS) technique to traverse a tree. Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level. 

Time Complexity : O(N)

## Why use it?
- Show levels top to bottom
- Show levels bottom to top
- Invert Binary Tree


## Concepts
- Tree Node
    ```
    class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
    ```
- 3 Queues
    1. Queue (Q) - LIFO : always append(Nodes), pop(0)
    2. Current Level (CL) - node = Q.pop(0). CL.append(node) shows left to right, CL.appendleft(node) shows right to left
    1. Result (R) - R.append(CL) shows tree top to bottom, R.appendleft(CL) shows bottom to top
- Iteration
    ```
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):

            ...
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    ```

## Complexity - Generally
- time complexity : O(V + E)
- space complexity : O(V)

## API
```
traverse(root)
```

## How its done
### Show Levels Top to Bottom

```
result, queue = [], deque()
if not root:
    return result
queue.append(root)
while queue:
    levelSize = len(queue)
    currentLevel = []
    for _ in range(levelSize):
        currentNode = queue.popleft()
        currentLevel.append(currentNode.val)
        if currentNode.left: #add children
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    result.append(currentLevel)
return result
```
### Show Levels Bottom to Top
Just change this line from above
```
result.appendleft(currentLevel) #just append left
```
### Mutate Linked List
```
def connect_level_order_siblings(root):
  queue = deque()
  queue.append(root)
  while queue:
    previous = None
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        if previous:
            previous.next = node
        previous = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
  return
```