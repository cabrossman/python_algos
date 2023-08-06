def cyclic_sort(nums):
    # counter = 0
    i = 0
    # while the counter < arr
    while i < len(nums):
        #swap -  - get value 
        # (a) get value at counter index.
        p1 = nums[i]
        # (b) get value at index (a)
        p2 = nums[p1-1]
        # put (b) in (a)'s index - which is the counter index
        nums[i] = p2
        # put (a) in its correct index (a)
        nums[p1-1] = p1

        # CHECK TO INCREMENT - if value at counter = counter
        if (i+1) == p2:
            i += 1
    return nums


def find_missing_number(nums):
    # ask if values aare indexed at 0 or 1 - determines if we need to adjust index or not
    # create indexes of first and last index in array
    i, n = 0, len(nums)

    # loop while first index is less than last
    while i < n:
        #get first index value
        p1_value = nums[i]
        #check that first index value is less than length of array and isnt its proper value
        if p1_value < n and nums[p1_value] != p1_value:
            #if it is not its proper value then cycle swap
            # 1) get value of index at p1_value ===> this equals p2_value
            # 2) put whatever was at p2 into current index i
            # 3) put the p1_value into its correct location at p1 value index
            p2_value = nums[p1_value]
            nums[i] = p2_value
            nums[p1_value] = p1_value
        else:
            # if it is then increment counter
            i += 1
    # iterate through "sorted" list and return the INDEX of the number that isnt is its place
    for i in range(n):
        if i != nums[i]:
            return i
    return 0

def find_missing_numbers(nums):
    # set index at 0 and len(list)
    i, n = 0, len(nums)
    # loop while i < len(list)
    while i < n:
        #get p1_value at index 
        p1_val = nums[i]
        #if p1_value < n and that its not in its correct spot then cycle swap
        if p1_val < (n+1) and p1_val != nums[p1_val-1]:
            p2_val = nums[p1_val-1]
            nums[i] = p2_val
            nums[p1_val-1] = p1_val
        # else increment
        else:
            i += 1
    # loop through and find numbers not in correct location and return list
    l = [i+1 for i in range(n) if (i+1)!=nums[i]]
    return l

def find_duplicate(nums):
    # index start and end
    i, n = 0, len(nums)
    # create set
    dups = set()
    # loop until index is larger than list
    while i < n:
        # check that value at index isnt in correct location
        if i+1 != nums[i]:
            # get value at index
            p1_val = nums[i]
            # check that value at index is already in its location
            # this indicates two numbers exist that cant fill that location
            if p1_val == nums[p1_val - 1]:
                # - if it is then add to dups and inc
                dups.add(p1_val)
                i += 1
            #   Otherwise - cycle swap
            else:
                p2_val = nums[p1_val - 1]
                nums[i] = p2_val
                nums[p1_val - 1] = p1_val
        # otherwise increment
        else:
            i += 1
    # return set
    return dups

assert cyclic_sort([3, 1, 5, 4, 2]) == [1, 2, 3, 4, 5]
assert cyclic_sort([2, 6, 4, 3, 1, 5]) == [1, 2, 3, 4, 5, 6]
assert cyclic_sort([1, 5, 6, 4, 3, 2]) == [1, 2, 3, 4, 5, 6]


assert find_missing_number([4, 0, 3, 1]) == 2
assert find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]) == 7

assert find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]) == [4, 6, 7]
assert find_missing_numbers([2, 4, 1, 2]) == [3]
assert find_missing_numbers([2, 3, 2, 1]) == [4]

assert find_duplicate([3, 4, 4, 5, 5]) == set([4, 5])
assert find_duplicate([5, 4, 7, 2, 3, 5, 3]) == set([3, 5])
print('all tests past!')