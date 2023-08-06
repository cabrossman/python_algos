# 15. Knapsack

## What is it?
0/1 Knapsack pattern is based on the famous problem with the same name which is efficiently solved using Dynamic Programming (DP).

Time Complexity of KnapSack = O(N * C)

## Why use it?
- Knapsack problem
- Equal Subset Sum (split list into two subsets and find equal sums)
- Overlapping sets

## Concepts
- DP = dynamic programming
- List of Lists

## Complexity
- time: O(N*W)
- space: O(N*W)

## API
```
solve_knapsack(profits, weights, capacity)
```

## How its done (all examples)
### 1. Setup and handle edge case
```
  ROWS = len(profits)
  COLUMNS = capacity + 1
  if len(profits) != len(weights) or capacity < 1:
    return 0
```
### 2. Create DP & set default (0 or False)
```
  dp = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
```
### 3. Mutate Defaults - for Knapsack we take all where capacity >= Weights in first row
```
  for c in range(COLUMNS):
    if c >= weights[0]:
      dp[0][c] = profits[0]
```
### 4. Iterate over all elements of DP. "Take" item if you have enough capacity and its higher than not taking item. Remember this for next iteration
```
  for i in range(1, ROWS): #0th row already iterated.
    for c in range(1, COLUMNS): #0th column has 0 capacity
      profit1, profit2 = 0, 0
      if c >= weights[i]:
        profit1 = profits[i] + dp[i - 1][c - weights[i]]
      profit2 = dp[i - 1][c]

      dp[i][c] = max(profit1, profit2)
```
### 5. Return bottom right
```
return dp[ROWS-1][COLUMNS-1]
```