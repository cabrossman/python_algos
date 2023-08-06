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
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:  # skip same element to avoid duplicate triplets
            continue
        left = i + 1
        right = len(arr) - 1
        while(left < right):
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:  # found the triplet
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:  # skip same element to avoid duplicate triplets
                    left += 1
                while left < right and arr[right] == arr[right + 1]:  # skip same element to avoid duplicate triplets
                    right -= 1
            elif current_sum < 0:
                left += 1  # we need a pair with a bigger sum
            else:
                right -= 1  # we need a pair with a smaller sum
    return triplets

assert tripplets([-3, 0, 1, 2, -1, 1, -2]) == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
assert tripplets([-5, 2, -1, -2, 3]) == [[-5, 2, 3], [-2, -1, 3]]
print('all tests past!')