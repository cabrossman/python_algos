class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(node, lower=float('-inf'), upper=float('inf')):
    if not node:
        return True
    if node.val <= lower or node.val >= upper:
        return False
    if not isValidBST(node.right, node.val, upper):
        return False
    if not isValidBST(node.left, lower, node.val):
        return False
    return True

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
assert isValidBST(root) == True

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)
assert isValidBST(root) == True
print('all tests passed')
