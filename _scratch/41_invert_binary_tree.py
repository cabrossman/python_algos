from collections import deque

def printTree(root):
    if root is None:
        print("Tree is empty.")
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        level_values = []
        all_none = True
        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level_values.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
                all_none = False
            else:
                level_values.append(None)
                queue.append(None)
                queue.append(None)
        if all_none:
            break
        print(level_values)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
printTree(root1)
invert_binary_tree(root1)
print("---------------")
printTree(root1)
