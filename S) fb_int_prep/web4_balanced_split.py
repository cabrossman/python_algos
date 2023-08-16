
def balancedSplitExists(arr):
    # Step 1: Sort the array & Init
    arr.sort()
    left, right = 0, len(arr) - 1
    sum_left, sum_right = arr[left], arr[right]

    while left < right - 1:  # We need a gap between the pointers
        if sum_left < sum_right:
            left += 1
            sum_left += arr[left]
        else:
            right -= 1
            sum_right += arr[right]
    # Check if the sums are equal and the left pointer is pointing to a smaller element
    return sum_left == sum_right and arr[left] < arr[right]

assert balancedSplitExists([1, 5, 7, 1]) == True
assert balancedSplitExists([12, 7, 6, 7, 6]) == False
assert balancedSplitExists([2, 1, 2, 5]) == True
assert balancedSplitExists([3, 6, 3, 4, 4]) == False

