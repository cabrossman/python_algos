"""
Given a binary tree and a number S, 
find all paths in the tree such that the 
sum of all the node values of each path equals S. 

Please note that the paths can start or end 
at any node but all paths must follow 
direction from parent to child (top to bottom).
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, _sum):
    all_paths = []
    cnt_paths_rec(root,  _sum,[], all_paths)
    return len(all_paths)

def cnt_paths_rec(root, _sum, current_path = [], all_paths = []):
    if root is None:
        return
    
    current_path.append(root.val)
    if root.left is None and root.right is None:
        #check if roots equal sum
        #loop backwards
        #if running tot == target then add to all paths
        tot = 0
        for i in range(len(current_path) - 1, -1, -1):
            tot += current_path[i]
            if tot == _sum:
                all_paths.append(1)
    else:
        left = cnt_paths_rec(root.left, _sum, current_path, all_paths)
        right = cnt_paths_rec(root.right, _sum, current_path, all_paths)
    current_path.pop()
    return

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert count_paths(root, 11) == 2
print('all tests have passed!')