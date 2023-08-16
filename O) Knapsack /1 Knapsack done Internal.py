"""
Given two integer arrays to represent weights and profits of N items, 
we need to find a subset of these items which will give us 
maximum profit such that their cumulative weight is not more than 
a given number C. Each item can only be selected once, 
which means either we put an item in the knapsack or we skip it.

"""

def solve_knapsack(profits, weights, capacity):
  ROWS = len(profits)
  COLUMNS = capacity + 1
  if len(profits) != len(weights) or capacity < 1:
    return 0

  #setup data and default to 0
  dp = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]

  #take all in first row
  for c in range(COLUMNS):
    if c >= weights[0]:
      dp[0][c] = profits[0]


  #for 1 to N rows (since we took all in first)
  for i in range(1, ROWS):
    #for 1 to C columns (since at 0 we take nothing)
    for c in range(1, COLUMNS):
      profit1, profit2 = 0, 0
      if c >= weights[i]:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      profit2 = dp[i - 1][c]

      dp[i][c] = max(profit1, profit2)


  return dp[ROWS-1][COLUMNS-1]

assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
print('all tests have passed!')
