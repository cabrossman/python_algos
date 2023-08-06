def has_triplets(arr):
    if len(arr) < 3:
        return False
    for mid, midV in enumerate(arr):
        if mid == 0:
            continue
        left, leftV = mid - 1, arr[mid - 1]
        right, rightV = len(arr) - 1, arr[len(arr) - 1]
        while mid < right:
            if leftV < midV and midV < rightV:
                return True
            if leftV > rightV: #it will never work so pull in
                right -= 1
                rightV = arr[right]
            else:
                mid += 1
                midV = arr[mid]
    return False

assert has_triplets([1, 2, 3, 4, 5]) == True
assert has_triplets([5, 4, 3, 2, 1]) == False
assert has_triplets([2, 1, 5, 0, 4, 6]) == True
assert has_triplets([1, 1, 1, 1, 1]) == False
assert has_triplets([10, 20, 5, 15, 30]) == True
assert has_triplets([3, 2, 1, 5, 0]) == False
assert has_triplets([5, 1, 5, 5, 2, 5, 4]) == True
assert has_triplets([1, 5, 0, 4, 2, 3]) == True
assert has_triplets([-2, -1, 0, 3, 5, 9]) == True
assert has_triplets([2, 4, 3, 2, 5, 4, 6]) == True
assert has_triplets([1]) == False
assert has_triplets([5, 7, 5, 4, 8]) == True
assert has_triplets([1, 0, 10, 0, 100]) == True
assert has_triplets([3, 3, 2, 0, 5, 9, 0, 7, 10]) == True
print('all tests have passed!')