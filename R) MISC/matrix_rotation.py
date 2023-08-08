"""
Rotate a matrix inplace like image rotation
"""

def rotate_image(matrix):
    # last row = first column, 2nd last = second column etc
    rows, cols = len(matrix), len(matrix[0])
    mat2 = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for c in range(cols):
            d_row = (rows - 1) - r
            mat2[c][r] = matrix[d_row][c]
    return mat2

m1_input = [[6, 9], [2, 7]]
m1_output = [[2, 6], [7, 9]]
m2_input = [[1]]
m2_output = [[1]]
m3_input = [[2, 14, 8], [12, 7, 14], [3, 3, 7]]
m3_output = [[3, 12, 2], [3, 7, 14], [7, 14, 8]]
assert rotate_image(m1_input) == m1_output
assert rotate_image(m2_input) == m2_output
assert rotate_image(m3_input) == m3_output

print('all test passed!')