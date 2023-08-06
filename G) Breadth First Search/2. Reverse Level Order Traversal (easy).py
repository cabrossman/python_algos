"""
Given a binary tree, populate an array to represent its level-by-level traversal 
in reverse order, i.e., the lowest level comes first. You should populate the 
values of all nodes in each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    result = deque()
    if not root:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        levelSize = len(queue)
        currentLevel = []
        for _ in range(levelSize):
            currentNode = queue.popleft()
            # add the node to the current level
            currentLevel.append(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.appendleft(currentLevel) #just append left
    result = list(result)
    return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert traverse(root) == [[9,10,5],[7,1],[12]]
print('all tests have passed!')