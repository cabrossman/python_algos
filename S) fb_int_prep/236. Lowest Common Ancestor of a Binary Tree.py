"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_LCA(root, p, q):
    if root is None:
        return
    
    if root.val in {p, q}:
        return root
    
    left_lca = find_LCA(root.left, p,q)
    right_lca = find_LCA(root.right, p,q)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
assert find_LCA(root, 5, 1).val == 3
assert find_LCA(root, 5, 6).val == 5

root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
assert find_LCA(root, 5, 4).val == 5
assert find_LCA(root, 6, 4).val == 5
