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

def main(fruit):
  start, max_count, fruit_count = 0, 0, {}
  for end in range(len(fruit)):
      fruit_count[ fruit[end] ] = fruit_count.get( fruit[end] ,0) + 1
      while len(fruit_count) > 2:
          fruit_count[ fruit[start] ] -= 1
          if fruit_count[ fruit[start] ] == 0:
              del fruit_count[ fruit[start] ]
          start += 1
      max_count = max(max_count, end - start + 1)
  return max_count

assert main(['A', 'B', 'C', 'A', 'C']) == 3
assert main(['A', 'B', 'C', 'B', 'B', 'C']) == 5
print('all tests past!')


