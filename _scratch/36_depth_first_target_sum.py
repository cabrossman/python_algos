class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path(root, target_sum):
    if root is None:
        return False
    
    is_leaf = True if root.left is None and root.right is None else False
    adj_sum = target_sum - root.val
    if is_leaf and adj_sum == 0:
        return True
    
    return has_path(root.left, adj_sum) or has_path(root.right, adj_sum)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert has_path(root, 23) == True
assert has_path(root, 16) == False
print('All tests have passed!')