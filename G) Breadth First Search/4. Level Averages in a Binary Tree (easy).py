"""
Given a binary tree, populate an array to represent the averages of all of its levels.
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
    while queue:
        levelSize = len(queue)
        currentLevel = deque()
        running_total = 0.0
        for _ in range(levelSize):
            currentNode = queue.popleft()
            running_total = running_total + currentNode.val
            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        result.append(running_total/levelSize)
    print(result)
    return list(result)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert traverse(root) == [12.0, 4.0, 6.5]
print('all tests have passed!')