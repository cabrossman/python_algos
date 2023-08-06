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


def find_paths_recursive(node, _sum, current_path, all_paths):
    if node is None:
        return
    current_path.append(node.val)

    is_leaf = True if node.left is None and node.right is None else False
    adj_sum = _sum - node.val
    
    if is_leaf and adj_sum == 0:
        all_paths.append(list(current_path))
    else:
        find_paths_recursive(node.left, adj_sum, current_path, all_paths)
        find_paths_recursive(node.right, adj_sum, current_path, all_paths)
    current_path.pop()
    return


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

res = []
expected = [[12, 7, 4], [12, 1, 10]]
find_paths_recursive(root, 23, current_path = [], all_paths = res) ## mutates res
assert res == expected
print('All tests have passed!')