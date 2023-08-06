"""
given a tree
    3
   / \
  9  20
    /  \
   15   7

return its order level traversal
[
  [3],
  [9,20],
  [15,7]
]
"""
class Tree:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# Create the nodes
node3 = Tree(3)
node9 = Tree(9)
node20 = Tree(20)
node15 = Tree(15)
node7 = Tree(7)

# Connect the nodes to form the binary tree
node3.left = node9
node3.right = node20
node20.left = node15
node20.right = node7

        
from collections import deque
def print_tree(root):
    lst = []
    if not root:
        return lst
    
    queue = deque()
    queue.append(root)
    while queue:
        level_len = len(queue)
        level_lst = []
        for _ in range(level_len):
            node = queue.popleft()
            level_lst.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        lst.append(level_lst)
    return lst

assert print_tree(node3) == [[3],[9,20],[15,7]]
print('all tests have passed')