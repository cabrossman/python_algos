"""
***HARD***


Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""

def tripplets(arr):
    arr.sort() # needed for dups
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i -1]:
            continue #dup found
        left = i + 1
        right = len(arr)-1
        while left < right:
            zsum = arr[i] + arr[left] + arr[right]
            triplets.append([arr[i], arr[left], arr[right]])
            if zsum == 0:
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1 #dup found
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1 #dup found
            elif zsum > 0:
                right -= 1
            else:
                left += 1
    return triplets
        
                


assert tripplets([-3, 0, 1, 2, -1, 1, -2], 0) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
assert tripplets([-5, 2, -1, -2, 3], 0) == [[-5, 2, 3], [-2, -1, 3]]
print('all tests past!')