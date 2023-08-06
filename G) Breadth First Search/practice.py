"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

class TreeNodeLL:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()

def traverse(root):
    # store result and check root is not none
    result = []
    if root is None:
        return result
    #create deque and append root (going to popleft)
    queue = deque()
    queue.append(root)

    # iterate while deque has nodes to process
    while queue:
        # iterate the length of current level - pop left one by one
        # get first node in list and store value in current level
        # add to deque the children of the node
        # add current level values to result
        # return after deque is empty
        current_level_len = len(queue)
        current_level_val = []
        for _ in range(current_level_len):
            current_node = queue.popleft()
            current_level_val.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        result.append(current_level_val)
    return result

def traverse_bottom_to_top(root):
    result = deque()
    queue = deque()
    queue.append(root)
    while queue:
        currentLevelLen = len(queue)
        currentLevelVal = []
        for _ in range(currentLevelLen):
            current_node = queue.popleft()
            currentLevelVal.append(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        result.appendleft(currentLevelVal)
    return list(result)

def connect_level_order_siblings(root):
  queue = deque()
  queue.append(root)
  while queue:
    previous = None
    level_size = len(queue)
    for _ in range(level_size):
        node = queue.popleft()
        if previous:
            previous.next = node
        previous = node

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
  return

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert traverse(root) == [[12],[7,1],[9,10,5]]

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert traverse_bottom_to_top(root) == [[9,10,5],[7,1],[12]]

print('all tests have passed!')

root = TreeNodeLL(12)
root.left = TreeNodeLL(7)
root.right = TreeNodeLL(1)
root.left.left = TreeNodeLL(9)
root.right.left = TreeNodeLL(10)
root.right.right = TreeNodeLL(5)
connect_level_order_siblings(root)

print("Level order traversal using 'next' pointer: ")
root.print_level_order()