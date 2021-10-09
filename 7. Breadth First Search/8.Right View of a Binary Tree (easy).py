"""
Given a binary tree, return an array containing nodes in its right view. 
The right view of a binary tree is the set of nodes visible when the 
tree is seen from the right side.
"""

from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ")
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next
    print()


def tree_right_view(root):
  result = []
  queue = deque()
  queue.append(root)
  previous = None
  while queue:
    level_size = len(queue)
    for i in range(level_size):
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        if i == level_size -1:
          result.append(node.val)
  return result


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(3)
result = tree_right_view(root)
assert result == [12, 1, 5, 3]
print('all tests have passed!')