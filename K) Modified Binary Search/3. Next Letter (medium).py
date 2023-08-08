"""
Given an array of lowercase letters sorted in ascending order, 
find the smallest letter in the given array greater than a given key.

Assume the given array is a circular list, 
which means that the last letter is assumed to be connected with the first letter. 
This also means that the smallest letter in the given array is greater than the 
last letter of the array and is also the first letter of the array.

Write a function to return the next letter of the given key.

Input: ['a', 'c', 'f', 'h'], key = 'f'
Output: 'h'
Explanation: The smallest letter greater than 'f' is 'h' in the given array.

Input: ['a', 'c', 'f', 'h'], key = 'b'
Output: 'c'
Explanation: The smallest letter greater than 'b' is 'c'.

Input: ['a', 'c', 'f', 'h'], key = 'm'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

Input: ['a', 'c', 'f', 'h'], key = 'h'
Output: 'a'
Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.

O(log N)
"""

def binary_search(arr, key):

    start, end = 0, len(arr) -1

    while start <= end:
        mid = (end - start)//2 + start
        if key < arr[mid]: 
            end = mid - 1
        else: #keep is greater than equal to mid
            start = mid + 1
    idx = start % len(arr) #start > end after while loop. loops around array
    return arr[idx]
    


assert binary_search(['a', 'c', 'f', 'h'], key = 'f') == 'h'
assert binary_search(['a', 'c', 'f', 'h'], key = 'b') == 'c'
assert binary_search(['a', 'c', 'f', 'h'], key = 'm') == 'a'
assert binary_search(['a', 'c', 'f', 'h'], key = 'h') == 'a'
print('all tests have passed!')