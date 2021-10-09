XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise. In other words, it only returns 1 if exactly one bit is set to 1 out of the two bits in comparison.

Input: 1, 5, 2, 6, 4
Answer: 3

A straight forward approach to solve this problem can be:

Find the sum of all integers from 11 to nn; lets call it s1.
Subtract all the numbers in the input array from s1; this will give us the missing number.

### What could go wrong
While finding the sum of numbers from 1 to nn, we can get integer overflow when nn is large.

Remember the important property of XOR that it returns 0 if both the bits in comparison are the same. In other words, XOR of a number with itself will always result in 0. This means that if we XOR all the numbers in the input array with all numbers from the range 11 to nn then each number in the input is going to get zeroed out except the missing number. Following are the set of steps to find the missing number using XOR:


XOR all the numbers from 1 to nn, lets call it x1.
XOR all the numbers in the input array, lets call it x2.
The missing number can be found by x1 XOR x2.

```
def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2

def main():
  arr = [1, 5, 2, 6, 4] 
  print('Missing number is:' + str(find_missing_number(arr)))

main()
```

### Important properties of XOR
Taking XOR of a number with itself returns 0, e.g.,
- 1 ^ 1 = 0
- 29 ^ 29 = 0
Taking XOR of a number with 0 returns the same number, e.g.,
- 1 ^ 0 = 1
- 31 ^ 0 = 31
XOR is Associative & Commutative, which means:
- (a ^ b) ^ c = a ^ (b ^ c)
- a ^ b = b ^ a

### OTher Notes
- number ^ complement = all_bits_set
- number ^ number ^ complement = number ^ all_bits_set
- 0 ^ complement = number ^ all_bits_set
- complement = number ^ all_bits_set
