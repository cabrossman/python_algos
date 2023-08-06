"""
Given a binary tree, populate an array to represent 
its zigzag level order traversal. 

You should populate the values of all nodes of the first level 
from left to right, then right to left for the next level 
and keep alternating in the same manner for the following levels.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
    result = deque()
    if not root:
        return list(result)
    
    queue = deque()
    queue.append(root)
    SWITCH = True
    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        for _ in range(levelSize):
            currentNode = queue.popleft()
            if SWITCH:
                currentLevel.append(currentNode.val)
            else:
                currentLevel.appendleft(currentNode.val)
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(list(currentLevel)) #just append left
        SWITCH = not SWITCH
    print(result)
    return list(result)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.right.left.left = TreeNode(20)
root.right.left.right = TreeNode(17)
assert traverse(root) == [[12],[1,7],[9,10,5],[17,20]]
print('all tests have passed!')