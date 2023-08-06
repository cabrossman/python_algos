
# Function to search a specific word in the grid
def word_search(grid, word):
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if depth_first_search(row, col, word, grid):
                return True
    return False

# Apply backtracking on every element to search the required word
def depth_first_search(row, col, word, grid):
    if len(word) == 0:
        return True

    c1 = row < 0 #outside grid
    c2 = row == len(grid) #outside grid
    c3 = col < 0 #outside grid
    c4 = col == len(grid[0]) #outside grid
    c5 = grid[row][col].lower() != word[0].lower() #doesnt match char
    if any([c1,c2,c3,c4,c5]):
        return False

    grid[row][col] = '*'

    for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]: #look around for next
        if depth_first_search(row + rowOffset, col + colOffset, word[1:], grid):
            return True

    grid[row][col] = word[0] #didnt find - put word back - backtracking

    return False


ex1 = [
    ["N","W","L","I","M"],
    ["V","I","L","Q","O"],
    ["O","L","A","T","O"],
    ["R","T","A","I","N"],
    ["O","I","T","N","C"]
    ]
ex2 = [
    ["J","D","E","I","Y"],
    ["G","I","L","M","O"],
    ["Z","A","I","E","O"],
    ["L","T","B","S","N"],
    ["S","I","T","C","C"]
    ]
ex3 = [
    ["H","D","L","I","M"],
    ["R","I","L","Z","O"],
    ["W","B","A","E","O"],
    ["H","U","K","V","N"],
    ["S","Y","E","D","C"]
]
assert word_search(ex1, "LATIN") == True
assert word_search(ex2, "AIM") == False
assert word_search(ex3, "BAKED") == True