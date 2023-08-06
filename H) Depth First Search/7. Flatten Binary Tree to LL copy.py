class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if root is None:
        return
    p1 = root
    while p1: #will manipulate node
        if p1.left: #check if there is a left side
            p2 = p1.left #set p2 to left side of p1 node
            while p2.right: #iterate to right most node
                p2 = p2.right
            p2.right = p1.right #copy right tree
            p1.right = p1.left # replace p1 right tree with left side of tree
            p1.left = None # set left side of tree to none
        p1 = p1.right #set p1 to p1.right to iterate
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