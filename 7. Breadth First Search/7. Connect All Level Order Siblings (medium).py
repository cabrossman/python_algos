"""
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to the first node of the next level.
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


def connect_all_siblings(root):
  queue = deque()
  queue.append(root)
  previous = None
  while queue:
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


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_all_siblings(root)
root.print_tree()