"""
Any number will be called a happy number if, after repeatedly replacing it with a number equal 
to the sum of the square of all of its digits, leads us to number '1'. 
All other (not-happy) numbers will never reach '1'. 
Instead, they will be stuck in a cycle of numbers which does not include '1'.

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

2^3 + 3^2 == 13
1^2 + 3^2 == 10
1^2 + 0^2 == 1

Input: 12   
Output: false (12 is not a happy number)  
Explanations: Here are the steps to find out that 12 is not a happy number:

Need to find if the constructed list has a cycle
"""
class Node:
  def __init__(self, v, n = None):
      self.value = v
      self.next = n
      self.sum_squares = sum(int(i)**2 for i in str(self.value))

  def has_cycle(self):
    slow, fast = self, self
    while fast and fast.next:
      fast = fast.next.next
      slow = slow.next
      if slow and fast and slow.value == fast.value:
        return True
    return False

def find_happy_number(num):
  head = Node(num)
  tail = Node(head.sum_squares)
  head.next = tail
  while not head.has_cycle():
    if tail.sum_squares == 1:
      return True
    tail.next = Node(tail.sum_squares)
    tail = tail.next
  return False

if __name__ == "__main__":
  assert find_happy_number(23) == True
  assert find_happy_number(12) == False

  print("all tests have past")