"""
Given two integer arrays to represent weights and profits of N items, 
we need to find a subset of these items which will give us 
maximum profit such that their cumulative weight is not more than 
a given number C. Each item can only be selected once, 
which means either we put an item in the knapsack or we skip it.

"""

def solve_knapsack(profits, weights, capacity):
    ROWS = len(profits)
    COLS = capacity + 1

    #dp
    dp =[[0 for c in range(COLS)] for r in range(ROWS)]
    
    #fill in first col
    for c in range(COLS):
        if c >= weights[0]:
            dp[0][c] = profits[0]

    #Next
    for r in range(1,ROWS):
        for c in range(1,COLS):
            p1, p2 = 0,0
            if c >= weights[r]:
                p1 = profits[r] + dp[r-1][c - weights[r]]
            p2 = dp[r-1][c]
            dp[r][c] = max(p1,p2)
    
    return dp[ROWS-1][COLS-1]

                
assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
print('all tests have passed!')
