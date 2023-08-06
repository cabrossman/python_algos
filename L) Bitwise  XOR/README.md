# 12. Bitwise XOR

## What is it?
XOR is a logical bitwise operator that returns 0 (false) if both bits are the same and returns 1 (true) otherwise.

## Why use it?
- Find missing number from array of non sorted integers. Doing so in the classical way can result in integer overflow, but XOR works without problem
- Find which number doesnt appear twice

## Concepts
### Taking XOR of a number with itself returns 0, e.g.,
```
1 ^ 1 = 0
29 ^ 29 = 0
```

### Taking XOR of a number with 0 returns the same number, e.g.,
```
1 ^ 0 = 1
31 ^ 0 = 31
```

### XOR is Associative & Commutative, which means:
```
(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
```

### Other Concepts
```
number ^ complement = all_bits_set
number ^ number ^ complement = number ^ all_bits_set
0 ^ complement = number ^ all_bits_set
complement = number ^ all_bits_set
```
## Complexity - Generally
- Time Complexity: XXX
- Auxiliary Space: XXX

## API
```
main(arr)
```

## How its done
### 1. Find missing Number
1. XOR all number from 1 to n - call this x1
2. XOR all the numbers in input array - call this x2
3. x1 ^ x2
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
```

### 2. Find single number in list of duplicates
```
from functools import reduce
reduce(lambda x, y: x ^ y, arr)
```

### 3. Other Variants
1. "#2" - Two numbers arent doubled example
2. Return compliment in base 10



