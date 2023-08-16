"""
Given a sorted array, create a new array containing squares of 
all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

"""

def main(l):
  left, right = 0, len(l) - 1
  sqrd = [n**2 for n in l]
  p_write = right
  while left < right:
    if sqrd[left] > sqrd[right]:
      l[p_write] = sqrd[left]
      left += 1
    else:
      l[p_write] = sqrd[right]
      right -=1
    p_write -=1
  l[p_write] = sqrd[left]
  return l

assert main([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
assert main([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]
print('all tests past!')