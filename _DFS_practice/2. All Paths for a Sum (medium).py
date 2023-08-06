"""
Given a binary tree and a number S, 
find all paths from root-to-leaf such that 
the sum of all the node values of each path equals S.

"""
from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root, required_sum):
  all_paths = []
  find_paths_recursive(root, required_sum, [], all_paths)
  return all_paths


def find_paths_recursive(root, _sum, current_path, all_paths):
  if root is None:
    return
  
  current_path.append(root.val)
  is_leaf = True if root.left is None and root.right is None else False
  adj_sum = _sum - root.val
  if is_leaf and adj_sum == 0:
    all_paths.append(list(current_path))
  else:# no return in this case so need else
    left = find_paths_recursive(root.left, adj_sum, current_path, all_paths)
    right = find_paths_recursive(root.right, adj_sum, current_path, all_paths)
  current_path.pop()
  return 
     
  


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert find_paths(root, 23) == [[12, 7, 4], [12, 1, 10]]
print('All tests have passed!')