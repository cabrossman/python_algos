"""
Given a matrix, mat, if any element within the matrix is zero, 
set that row and column to zero.
"""

def set_matrix_zeros(mat):
    rows = len(mat)
    cols = len(mat[0])

    row_set = set()
    col_set = set()
    for row in range(rows):
        for col in range(cols):
            if mat[row][col] == 0:
                row_set.add(row)
                col_set.add(col)
    
    for row in range(rows):
        for col in range(cols):
            if row in row_set or col in col_set:
                mat[row][col] = 0

    return mat

m1_input = [[1,2,3],[4,5,6],[7,0,9]]
m1_output = [[1, 0, 3], [4, 0, 6], [0, 0, 0]]
m2_input = [[1,2,3,4],[4,5,6,7],[8,9,4,6]]
m2_output = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 4, 6]]
m3_input = [[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,1,1,1],[1,1,1,1,1]]
m3_output = [[0, 0, 0, 0, 0], [1, 0, 0, 1, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 1, 1]]
assert set_matrix_zeros(m1_input) == m1_output
assert set_matrix_zeros(m2_input) == m2_output
assert set_matrix_zeros(m3_input) == m3_output

print('all test passed!')