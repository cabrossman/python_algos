"""
Given a binary tree, find the length of its diameter. 
The diameter of a tree is the number of nodes on the 
longest path between any two leaf nodes. 
The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

"""

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def diameter(node):
    if node is None:
        return 0, 0
    H_left, D_left = diameter(node.left)
    H_right, D_right = diameter(node.right)
    potential_d = H_left + H_right + 1

    height = max(H_left, H_right) + 1
    diameter_ = max(potential_d, D_left, D_right)
    return height, diameter_

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(5)
h, d = diameter(root)
assert d == 5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
h, d = diameter(root)
assert d == 5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
h, d = diameter(root)
assert d == 7
print('tests have passed!')