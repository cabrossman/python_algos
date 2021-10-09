"""
Given two integer arrays to represent weights and profits of N items, 
we need to find a subset of these items which will give us 
maximum profit such that their cumulative weight is not more than 
a given number C. Each item can only be selected once, 
which means either we put an item in the knapsack or we skip it.

"""

def solve_knapsack(profits, weights, capacity):
  # create a two dimensional array for Memoization, each element is initialized to '-1'
  dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
  return knapsack_recursive(dp, profits, weights, capacity, 0, '')


def knapsack_recursive(dp, profits, weights, capacity, currentIndex, logger):
  logger = logger + ' ->'
  print(f'{logger} capacity: {capacity} index : {currentIndex}')
  # base checks
  if capacity <= 0 or currentIndex >= len(profits):
    return 0

  # if we have already solved a similar problem, return the result from memory
  if dp[currentIndex][capacity] != -1:
    return dp[currentIndex][capacity]

  # recursive call after choosing the element at the currentIndex
  # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
  profit1 = 0
  if weights[currentIndex] <= capacity:
    profit1 = profits[currentIndex] + knapsack_recursive(
        dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1, logger)
    print(f'{logger} capacity: {capacity} index : {currentIndex} ||| profit1 : {profit1}')

  # recursive call after excluding the element at the currentIndex
  profit2 = knapsack_recursive(dp, profits, weights, capacity, currentIndex + 1, logger)
  print(f'{logger} capacity: {capacity} index : {currentIndex} ||| profit2 : {profit2}')

  profit = max(profit1, profit2)
  dp[currentIndex][capacity] = profit
  return profit


assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6) == 17
assert solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7) == 22
