"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  result = []
  if not root:
    return result
  
  queue = deque()
  queue.append(root)
  while queue:
    level_len = len(queue)
    level = []
    for _ in range(level_len):
      node = queue.popleft()
      level.append(node.val)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    result.append(level)
  return result

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert traverse(root) == [[12],[7,1],[9,10,5]]
print('all tests have passed!')