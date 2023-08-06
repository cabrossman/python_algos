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
    left = find_LCA(root.left, p, q)
    right = find_LCA(root.right, p, q)
    if left and right:
        return root
    return left if left else right

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
