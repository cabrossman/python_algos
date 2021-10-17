"""
Given an array of characters where each character represents a fruit tree, you are given two baskets, 
and your goal is to put maximum number of fruits in each basket. 
The only restriction is that each basket can have only one type of fruit.

You can start with any tree, 
but you cant skip a tree once you have started. 
You will pick one fruit from each tree until you cannot, 
i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

O(N + N) ~= O(N)
"""

def main(s,k=2):
  window_start, largest_sub_array = 0, 0
  for window_end in range(len(s)):
    sub = s[window_start:window_end + 1]
    while len(sub) > k and window_start < window_end:
      if len(set(sub)) == 2:
        largest_sub_array = max(largest_sub_array, window_end - window_start + 1)
        break
      window_start = window_start + 1
      sub = s[window_start:window_end + 1]
  return largest_sub_array


assert main(['A', 'B', 'C', 'A', 'C']) == 3
assert main(['A', 'B', 'C', 'B', 'B', 'C']) == 5
print('all tests past!')


