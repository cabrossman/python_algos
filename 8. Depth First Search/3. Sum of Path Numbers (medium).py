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
  find_paths_recursive(
        currentNode = root, 
        current_path = '',
        all_paths = all_paths
        )
  return sum(path for path in all_paths)


def find_paths_recursive(currentNode, current_path, all_paths):
    if currentNode is None:
        return

    # add the current node to the path
    current_path = current_path + str(currentNode.val)

    # terminal path - all leaves
    if (
        not currentNode.left 
        and not currentNode.right
    ):
        all_paths.append(int(current_path))
    else:
        # traverse the left sub-tree
        find_paths_recursive(
            currentNode = currentNode.left, 
            current_path = current_path,
            all_paths = all_paths
        )
        # traverse the right sub-tree
        find_paths_recursive(
            currentNode = currentNode.right, 
            current_path = current_path,
            all_paths = all_paths
        )
    # remove the current node from the path to backtrack,
    # we need to remove the current node while we are going up the recursive call stack.
    current_path = str(current_path[:-1])


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
assert find_sum_of_path_numbers(root) == 332
print('All tests have passed!')