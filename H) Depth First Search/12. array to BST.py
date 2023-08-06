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

def sortedArrayToBST(nums):
    if not nums:
        return None
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    
    return root

nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
printTree(root)
