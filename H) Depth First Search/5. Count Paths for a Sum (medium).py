"""
Given a binary tree and a number S, 
find all paths in the tree such that the 
sum of all the node values of each path equals S. 

Please note that the paths can start or end 
at any node but all paths must follow 
direction from parent to child (top to bottom).
"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, _sum):
    all_paths = []
    cnt_paths_rec(
        node = root, 
        _sum = _sum,
        current_path = [], 
        all_paths = all_paths #gonna mutate this fucker
    )
    return len(all_paths)

def cnt_paths_rec(node, _sum, current_path = [], all_paths = []):
    if not node:
        return

    current_path.append(node.val)

    #if leaf check if any sums make it
    if (
        not node.left
        and not node.right
    ):
        tot = 0
        for val in current_path[::-1]:
            tot = tot + val
            if tot == _sum:
                all_paths.append(list(current_path))
    else:
        #search left
        cnt_paths_rec(
            node = node.left, 
            _sum = _sum,
            current_path = current_path, 
            all_paths = all_paths #gonna mutate this fucker
        )
        #search right
        cnt_paths_rec(
            node = node.right, 
            _sum = _sum,
            current_path = current_path, 
            all_paths = all_paths #gonna mutate this fucker
        )
    del current_path[-1]



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
assert count_paths(root, 11) == 2
print('all tests have passed!')