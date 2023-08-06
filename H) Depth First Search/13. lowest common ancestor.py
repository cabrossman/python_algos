class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_LCA(root, p, q):
    if root is None:
        return
    # If either p or q is the root, root is the LCA
    if root.val == p or root.val == q:
        return root
    # Search for LCA in the left and right subtrees
    left_lca = find_LCA(root.left, p, q)
    right_lca = find_LCA(root.right, p, q)
    # If p and q are found in left and right subtrees of current node, 
    # then the current node is the LCA
    if left_lca and right_lca:
        return root
    # Otherwise, return the non-empty child
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
