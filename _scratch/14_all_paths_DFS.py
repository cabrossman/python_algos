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


def find_paths_recursive(currentNode, _sum, current_path, all_paths):
   if currentNode is None:
      return
   
   current_path.append(currentNode.val)
   
   hit_targ = _sum == currentNode.val
   no_left = currentNode.left is None
   no_right = currentNode.right is None
   if all([hit_targ, no_left, no_right]):
      all_paths.append(list(current_path))

   find_paths_recursive(
      currentNode = currentNode.left,
      _sum = _sum - currentNode.val,
      current_path = current_path,
      all_paths = all_paths
   )

   find_paths_recursive(
      currentNode = currentNode.right,
      _sum = _sum - currentNode.val,
      current_path = current_path,
      all_paths = all_paths
   )

   del current_path[-1]



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert find_paths(root, 23) == [[12, 7, 4], [12, 1, 10]]
print('All tests have passed!')