"""
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. 
Find the total sum of all the numbers represented by all paths.
"""
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_sum_of_path_numbers(root):
  all_paths = []
  find_paths_recursive(root,[],all_paths)
  return sum(path for path in all_paths)


def find_paths_recursive(root, current_path, all_paths):
  if root is None:
    return
  
  current_path.append(str(root.val))
  if root.left is None and root.right is None:
    all_paths.append(int(''.join(current_path)))
  else:
    left = find_paths_recursive(root.left, current_path, all_paths)
    right = find_paths_recursive(root.right, current_path, all_paths)
  current_path.pop()
  return

    
root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
assert find_sum_of_path_numbers(root) == 332
print('All tests have passed!')