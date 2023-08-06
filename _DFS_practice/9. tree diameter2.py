class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def depth_and_diameter(node):
    
    """
    left_diameter: The longest path between any two nodes in the left subtree. 
    -> This represents the case where the diameter does 
    -> not include the current node and is entirely contained within the left subtree.

    same on right

    left_depth + right_depth: The longest path between any two nodes that 
    passes through the current node. This is computed as the sum of the 
    depths of the left and right subtrees because you're connecting the 
    deepest nodes of the left subtree to the deepest nodes of the right 
    subtree via the current node.
    """
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(5)

depth, diameter = depth_and_diameter(root)
assert diameter == 4

print('tests have passed!')