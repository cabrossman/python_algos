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


def height(node):   
    if node is None: # Base Case : Tree is empty
        return 0
    left_h = height(node.left)
    right_h = height(node.right)
    return 1 + max(left_h, right_h)

def diameter(root):   
    if root is None: # Base Case when tree is empty
        return 0
    
    left_max_h = height(root.left)
    right_max_h = height(root.right)
    potential_diam = left_max_h + right_max_h + 1
 
    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)
    # Return max of the following tree: subtree_diam of left or right / Height
    return max(ldiameter, rdiameter, potential_diam)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
assert diameter(root) == 5
root.left.left = None
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
root.right.left.right.left = TreeNode(10)
root.right.right.left.left = TreeNode(11)
assert diameter(root) == 7
print('all tests have passed')
