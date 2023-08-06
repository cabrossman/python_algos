class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def max_depth(root):
    #each leaf will have 0 on left & right and return a value of one
    # # as we pop up the stack instead of left being 0 it will be the
    # # runing total of its count of children
    if root is None:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(5)
assert max_depth(root) == 4