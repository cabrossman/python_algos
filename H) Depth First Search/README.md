# 8. Depth First Search

## What is it?
Depth First Search (DFS) technique to traverse a tree.
We will be using recursion (or we can also use a stack for the iterative approach) to keep track of all the previous (parent) nodes while traversing.

Time Complexity : O(N^2)

## Why use it?
- Binary Tree Path Sum
- All Paths for a Sum
- A sum of Path Numbers
- A path with given sequence
- Count Paths for a Sum
- Tree Diameter

## Concepts
- Tree Node
    ```
    class TreeNode:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    ```
- Recursion
    0. Pass external list to outside function to append to
    1. Handle Edge cases & Terminal Case
    2. Handle path for `left` and path for `right`
    3. To keep state pass a named list into the head of recursive function
    4. IF a SUM subtract values on recursive calls
    5. No work is done until leaf nodes and we pop up the stack. 

- Depth First Search
    1. Go deepest to terminal node and then go wide

## Complexity - Generally
- time complexity : O(V + E)
- space complexity : O(V)

## API
```
traverse(root)
```

## How its done
### Binary Tree Path Sum
```
def has_path(root, _sum):
  if not root:
    return False
  if (
        root.val == _sum  
        and not root.left 
        and not root.right
    ): # terminal path
        return True
  return has_path(root.left, _sum - root.val) or has_path(root.right, _sum - root.val)
```
### All Paths for a Sum
```
    if currentNode is None:
        return

    # add the current node to the path
    current_path.append(currentNode.val)

    # terminal path
    if (
        currentNode.val == _sum 
        and not currentNode.left 
        and not currentNode.right
    ):
        all_paths.append(list(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(
            currentNode = currentNode.left, 
            _sum = _sum - currentNode.val, 
            current_path = current_path,
            all_paths = all_paths
        )
        # traverse the right sub-tree
        find_paths_recursive(
            currentNode = currentNode.right, 
            _sum = _sum - currentNode.val, 
            current_path = current_path,
            all_paths = all_paths
        )
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    del current_path[-1]
```
### Path with a given sequence
```
if not root:
    return False
current_seq.append(root.val)
if current_seq == sequence:
    return True
else:
    left = find_path(root = root.left,sequence = sequence,current_seq = current_seq)
    right = find_path(root = root.right,sequence = sequence, current_seq = current_seq)
del current_seq[-1]
return left or right
```
### Count the Sum of Paths. 
Make sure to sum the paths at a terminal node
```
if (not node.left and not node.right):
    tot = 0
    for val in current_path[::-1]: #iterate backwards (or pop)
        tot = tot + val
        if tot == _sum:
            all_paths.append(list(current_path))
```