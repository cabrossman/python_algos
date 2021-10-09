# Notes


```
  quadruplets = set()
  arr.sort()
  for i in range(len(arr) - 2):
    left = i + 1
    right = len(arr) -1
    while(left < right):
       ...
       if too high:
        left = left + 1
       if too low:
         right = right -1
```


https://www.educative.io/courses/grokking-the-coding-interview/xlK78P3Xl7E

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. So, to try more pairs, we can decrement the end-pointer.

If the sum of the two numbers pointed by the two pointers is smaller than the target sum, this means that we need a pair with a larger sum. So, to try more pairs, we can increment the start-pointer.


