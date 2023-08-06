def merge_sort(arr):
    if len(arr) <= 1:
        return arr # If the input array has one or zero elements, it's already sorted
    
    mid = len(arr) // 2
    left = arr[:mid]  # Divide the array into two halves
    right = arr[mid:]

    left = merge_sort(left) # Sort the left half recursively
    right = merge_sort(right) # Sort the right half recursively

    return merge(left, right) # Merge the sorted halves

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # While there are elements in both left and right arrays
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # If there are remaining elements in the left array, append them to the result
    while left_idx < len(left):
        result.append(left[left_idx])
        left_idx += 1

    # If there are remaining elements in the right array, append them to the result
    while right_idx < len(right):
        result.append(right[right_idx])
        right_idx += 1

    return result

# Assertions with test cases to verify the code

assert merge_sort([5, 3, 4, 1, 2]) == [1, 2, 3, 4, 5]
assert merge_sort([100, -3, 2, 3, 0, -10]) == [-10, -3, 0, 2, 3, 100]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
