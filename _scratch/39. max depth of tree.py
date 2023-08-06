class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def max_depth(root):
  if root is None:
    return 0
  left = max_depth(root.left)
  right = max_depth(root.right)
  return max(left, right) + 1
  

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(5)
assert max_depth(root) == 4
print('all tests have passed!')