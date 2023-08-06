"""
Given a sorted array, create a new array containing squares of 
all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]

"""


def main(l):
  left = 0
  right = len(l) - 1
  nl = [0 for i in range(len(l))]
  nl_index = right
  while left < right:
    if abs(l[right]) >= abs(l[left]):
      nl[nl_index] = l[right]**2
      right = right - 1
      nl_index = nl_index - 1
    else:
      nl[nl_index] = l[left]**2
      left = left + 1
      nl_index = nl_index - 1
  return nl


assert main([-2, -1, 0, 2, 3]) == [0, 1, 4, 4, 9]
assert main([-3, -1, 0, 1, 2]) == [0, 1, 1, 4, 9]
print('all tests past!')