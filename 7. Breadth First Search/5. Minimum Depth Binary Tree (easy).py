"""
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest 
path from the root node to the nearest leaf node.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    if not root:
        return 0
    
    queue = deque()
    queue.append(root)
    levels = 0
    while queue:
        levelSize = len(queue)
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        levels = levels + 1
    print(levels - 1)
    return levels - 1


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert find_minimum_depth(root) == 2
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
assert find_minimum_depth(root) == 3
print('all tests have passed!')