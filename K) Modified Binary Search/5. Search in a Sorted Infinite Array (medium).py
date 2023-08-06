"""
Given an infinite sorted array (or an array with unknown size), 
find if a given number key is present in the array. 

Write a function to return the index of the key if it is present in the array, otherwise return -1.

Since it is not possible to define an array with infinite (unknown) size, 
you will be provided with an interface ArrayReader to read elements of the array. 
ArrayReader.get(index) will return the number at index; if the array's size is smaller than the index, 
it will return Integer.MAX_VALUE.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 16
Output: 6
Explanation: The key is present at index '6' in the array.

Input: [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30], key = 11
Output: -1
Explanation: The key is not present in the array.

Input: [1, 3, 8, 10, 15], key = 15
Output: 4
Explanation: The key is present at index '4' in the array.

Input: [1, 3, 8, 10, 15], key = 200
Output: -1
Explanation: The key is not present in the array.

O(log N + log N) = O(log N)
"""

import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def binary_search(reader, key, start, end):
    while start <= end:
        mid = (end - start)//2 + start
        val = reader.get(mid)
        if key > val:
            start = mid + 1
        elif key < val:
            end = mid - 1
        else:
            return mid
    return -1

def search_in_infinite_array(reader, key):
    start, end = 0,1
    while reader.get(end) < key:
        start = end + 1
        end = (end + 1)*2

    return binary_search(reader, key, start, end)


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
search_in_infinite_array(reader, 16) == 6
assert search_in_infinite_array(reader, 11) == -1
reader = ArrayReader([1, 3, 8, 10, 15])
assert search_in_infinite_array(reader, 15) == 4
assert search_in_infinite_array(reader, 200) == -1
print('all tests have passed!')