def search(nums, target):
    low, high = 0, len(nums) -1
    while low <= high:
        mid = (high - low)//2 + low
        if nums[mid] == target:
            return mid
        #if lower sorted
        if nums[low] <= nums[mid]:
            #check to see if key is lower half
            if nums[low] <= target and target < nums[mid]: 
                high = mid - 1
            else:
                low = mid + 1
        #else (lower not sorted) - upper may not be sorted
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

assert search([6,7,1,2,3,4,5], 1) == 2
assert search([10,11,12,13,1,2,3], 12) == 2
print('all tests have passed!')