class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def depth_and_diameter(node):
  if node is None:
    return 0, 0
  
  lh_depth, lh_diameter = depth_and_diameter(node.left)
  rh_depth, rh_diameter = depth_and_diameter(node.right)

  diameter = max(lh_diameter, rh_diameter, lh_depth + rh_depth)
  depth = max(lh_depth, rh_diameter) + 1
  return depth, diameter


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(5)

depth, diameter = depth_and_diameter(root)
assert diameter == 4

print('tests have passed!')