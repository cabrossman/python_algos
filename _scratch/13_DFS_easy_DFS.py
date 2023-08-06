"""
Given a binary tree and a number S, 
find if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path equals S.

"""
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, _sum):
  if root is None:
     return False
  
  #terminal
  found_sum = root.val == _sum
  null_left = root.left is None
  null_right = root.right is None
  if all([found_sum, null_left, null_right]):
     return True
  
  #traverse
  left = has_path(root.left, _sum - root.val)
  if left:
     return True
  right = has_path(root.right, _sum - root.val)
  if right:
     return True
  return False
    


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert has_path(root, 23) == True
assert has_path(root, 16) == False
print('All tests have passed!')