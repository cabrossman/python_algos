"""
Given an n x n binary matrix grid, 
return the length of the shortest clear path in the matrix. 
If there is no clear path, return -1.

A clear path in a binary matrix is a path from the 
top-left cell (i.e., (0, 0)) to the bottom-right 
cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected 
(i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
"""
from collections import deque
def shortest_path(grid):
    n = len(grid)
    directions = [
        (0,1), #right
        (1,1), #diag right
        (1,0), #down
        (1,-1), #diag left
        (0, -1), #left
        (-1, -1), #diag upper left
        (-1, 0), #up
        (-1, 1), #diag upper right
    ]
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    queue = deque() #(row, col, path length)
    queue.append((0,0,1))
    grid[0][0] = 1 #mark as visited
    while queue:
        (row, col, path_len) = queue.popleft()
        if row == n-1 and col == n-1:
            return path_len
        for row_adj, col_adj in directions:
            new_row, new_col = row + row_adj, col + col_adj
            valid_move = 0 <= new_row < n and 0 <= new_col < n
            if valid_move and grid[new_row][new_col] == 0:
                queue.append((new_row, new_col, path_len + 1))
                grid[new_row][new_col] = 1 #check we dont revist
    return -1

assert shortest_path([[0,1],[1,0]]) == 2
assert shortest_path([[0,0,0],[1,1,0],[1,1,0]]) == 4
assert shortest_path([[1,0,0],[1,1,0],[1,1,0]]) == -1
assert shortest_path([[0,0,0],[0,1,0],[0,0,0]]) == 4
assert shortest_path([[0,0,0],[0,1,0],[1,0,0]]) == 4
assert shortest_path([[0]]) == 1
assert shortest_path([[1]]) == -1
print('all tests have passed!')
