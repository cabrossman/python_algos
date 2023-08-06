"""
Given a binary tree and a number sequence, 
find if the sequence is present as a root-to-leaf path in the given tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence, current_seq = []):
    if root is None:
        return False
    
    current_seq.append(root.val)
    if current_seq == sequence:
        return True
    left = find_path(root.left, sequence, current_seq)
    right = find_path(root.right, sequence, current_seq)
    if left or right:
        return True
    current_seq.pop()
    return False
    

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

assert find_path(root, [1, 0, 7]) == False
assert find_path(root, [1, 1, 6]) == True
print('all tests have passed!')