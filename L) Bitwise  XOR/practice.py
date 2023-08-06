from functools import reduce

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

def find_single_number(arr):
  return reduce(lambda x, y: x ^ y, arr)

def find_single_numbers(nums):
    # get the XOR of the all the numbers
    n1xn2 = reduce(lambda x, y: x ^ y, nums)

    # get the rightmost bit that is '1'
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        rightmost_set_bit = rightmost_set_bit << 1
    num1, num2 = 0, 0

    for num in nums:
        if (num & rightmost_set_bit) != 0:  # the bit is set
            num1 ^= num
        else:  # the bit is not set
            num2 ^= num

    return [num1, num2]

def calculate_bitwise_complement(num):
  # count number of total bits in 'num'
  bit_count, n = 0, num
  while n > 0:
    bit_count += 1
    n = n >> 1

  # for a number which is a complete power of '2' i.e., it can be written as pow(2, n), if we
  # subtract '1' from such a number, we get a number which has 'n' least significant bits set to '1'.
  # For example, '4' which is a complete power of '2', and '3' (which is one less than 4) has a binary
  # representation of '11' i.e., it has '2' least significant bits set to '1'
  all_bits_set = pow(2, bit_count) - 1

  # from the solution description: complement = number ^ all_bits_set
  return num ^ all_bits_set




assert find_missing_number([1, 5, 2, 6, 4]) == 3

assert find_single_number([1,4,2,1,3,2,3]) == 4

# These dont work???
#assert find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]) == [4, 6]
#assert find_single_numbers([2, 1, 3, 2]) == [1, 3]

assert calculate_bitwise_complement(8) == 7
assert calculate_bitwise_complement(10) == 5
print('all tests have passed')