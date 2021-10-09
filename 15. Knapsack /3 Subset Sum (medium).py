"""
  Given a set of positive numbers, 
  determine if a subset exists whose 
  sum is equal to a given number S.

  Input: {1, 2, 3, 7}, S=6
  Output: True
  The given set has a subset whose sum is '6': {1, 2, 3}

  Input: {1, 2, 7, 1, 5}, S=10
  Output: True
  The given set has a subset whose sum is '10': {1, 2, 7}

  Input: {1, 3, 4, 8}, S=6
  Output: False
  The given set does not have any subset whose sum is equal to '6'.


  same problem as #2- just given sum
"""

def can_partition(num, zsum):
  COLUMNS = zsum + 1
  ROWS = len(num)
  dp = [[False for _ in range(COLUMNS)] for _ in range(ROWS)]

  # fill in 0 sum with True
  for row in range(ROWS):
    dp[row][0] = True

  # test if 1st column equals the sum
  for zsum in range(COLUMNS):
    if zsum == num[0]:
      dp[0][zsum] = True

  
  #dynamic programming
  for row in range(1, ROWS):
    for zsum in range(1, COLUMNS):
      #if it was true in above row its true in current
      if dp[row - 1][zsum]:
        dp[row][zsum] = True
      # if not true - check if higher capacity
      elif zsum >= num[row]:  # else if we can find a subset to get the remaining sum
        dp[row][zsum] = dp[row - 1][zsum - num[row]]

  return dp[ROWS-1][COLUMNS-1]


can_partition([1, 2, 3, 7], 6) == True
can_partition([1, 2, 7, 1, 5], 10) == True
can_partition([1, 3, 4, 8], 6) == False

print('all tests have passed')