
def has_triplets(nums):
    """
    has to be in order so we take advantage of that here
    first = smallest num seen in past
    second => a current number greater than first
    found => x > second > first
    
    """
    if len(nums) < 3:
        return False
    first, second = float('inf'), float('inf')
    for n in nums: # case on which smaller. increasing.
        if n <= first:
            first = n
        elif n <= second:# first < (n <= second) < third
            second = n
        else:  # first < second < third
            return True
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