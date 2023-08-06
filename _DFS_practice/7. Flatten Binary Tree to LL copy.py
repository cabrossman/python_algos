class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if root is None:
        return
    p1 = root
    while p1:
        if p1.left:
            p2 = p1.left
            while p2.right: p2 = p2.right
            p2.right = p1.right
            p1.left, p1.right = None, p1.left
        p1 = p1.right
    return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(6)

flatten(root)

current = root
while current:
    print(current.val)
    current = current.right