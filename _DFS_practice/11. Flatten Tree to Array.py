class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root, data):
    if root is None:
        return
    data.append(root.val)
    flatten(root.left, data)
    flatten(root.right, data)
    return

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

res = []
flatten(root, res)
assert res == [1,2,3,4,5,6]
print('all tests have passed!')