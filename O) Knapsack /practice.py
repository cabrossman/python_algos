"""
Given two integer arrays to represent weights and profits of N items, 
we need to find a subset of these items which will give us 
maximum profit such that their cumulative weight is not more than 
a given number C. Each item can only be selected once, 
which means either we put an item in the knapsack or we skip it.
"""

def solve_knapsack(profits, weights, capacity):
  #Setup pointers and handle edge cases
  ## Rows = Profit, Cols = Capacity
  ## Handle edge if profits != weights (return 0)
  R_PROFIT = len(profits)
  C_CAPACITY = capacity + 1
  if len(profits) != len(weights):
    return 0

  # Create Dynamic Array
  ## init to 0 and first row = profit if capacity exists
  dp = [[0 for _ in range(C_CAPACITY)] for _ in range(R_PROFIT)]
  for c_cap in range(C_CAPACITY):
    if c_cap >= weights[0]:
      dp[0][c_cap] = profits[0]

  #CORE ALGO
  #ROWS = for 1 to len(profit) - since we took all in first row above
  ##COLS - for 1 to C columns - since we consider 0 capacity
  ## reset profit pointers
  ### if capacity >= cost to carry item
  #### if so profit1 = profit of current item + profit at excess capacity
  ######## profit @excess => prior row, col = current capacity - current weight
  ### second profit => prior row at current capacity
  ## update dynamic prog array at current row & col = max(two profit optoins)
  for r_prof in range(1, R_PROFIT):
    for c_cap in range(1, C_CAPACITY):
      profit1, profit2 = 0,0
      if c_cap >= weights[r_prof]:
        profit1 = profits[r_prof] + dp[r_prof - 1][c_cap - weights[r_prof]]
      profit2 = dp[r_prof - 1][c_cap]
      dp[r_prof][c_cap] = max(profit1, profit2)


  # return last row column to optimal profit
  return dp[R_PROFIT -1][C_CAPACITY -1]

assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
print('all tests have passed!')