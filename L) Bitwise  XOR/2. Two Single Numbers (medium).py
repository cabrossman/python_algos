"""
In a non-empty array of numbers, 
every number appears exactly twice except two numbers that appear only once. 
Find the two numbers that appear only once.

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

Input: [2, 1, 3, 2]
Output: [1, 3]
"""
from functools import reduce

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

arr = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
assert find_single_numbers(arr) == [4, 6]

arr = [2, 1, 3, 2]
assert find_single_numbers(arr) == [1, 3]
print('all tests have passed')