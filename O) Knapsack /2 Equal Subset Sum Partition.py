"""
    Given a set of positive numbers, find if we can partition 
    it into two subsets such that the sum of elements in 
    both subsets is equal.

    Input: {1, 2, 3, 4}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}

    Input: {1, 1, 3, 4, 7}
    Output: True
    Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}

    Input: {2, 3, 4, 6}
    Output: False
    Explanation: The given set cannot be partitioned into two subsets with equal sum.
"""

def can_partition(num):
  s = sum(num)
  # if 's' is a an odd number, we can't have two subsets with same total
  if s % 2 != 0:
    return False

  # we are trying to find a subset of given numbers that has a total sum of 's/2'.
  s = int(s / 2)
  COLUMNS = s + 1
  ROWS = len(num)

  dp = [[False for x in range(COLUMNS)] for y in range(ROWS)]

  # populate the s=0 columns, as we can always for '0' sum with an empty set
  for i in range(0, ROWS):
    dp[i][0] = True

  # with only one number, we can form a subset only when the required sum is
  # equal to its value
  for j in range(1, COLUMNS):
      if num[0] == j:
        dp[0][j] = True

  # process all subsets for all sums
  for i in range(1, ROWS):
    for zsum in range(1, COLUMNS):
      # if we can get the sum 'j' without the number at index 'i'
      if dp[i - 1][zsum]:
        dp[i][zsum] = True
      elif zsum >= num[i]:  # else if we can find a subset to get the remaining sum
        dp[i][zsum] = dp[i - 1][zsum - num[i]]

  # the bottom-right corner will have our answer.
  return dp[ROWS - 1][COLUMNS - 1]


can_partition([1, 2, 3, 4]) == True
can_partition([1, 1, 3, 4, 7]) ==  True
can_partition([2, 3, 4, 6]) == False
print('all tests have passed')