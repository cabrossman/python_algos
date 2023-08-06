def search(nums, target):
    low, high = 0, len(nums) -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]: #bottom half sorted
            if nums[low] <= target and target < nums[mid]: #low <= target < mid
                high = mid - 1 
            else:
                low = mid + 1 
        else: #bottom half not sorted
            if nums[mid] < target and target <= nums[high]: #mid < target <= high
                low = mid + 1
            else:
                high = mid - 1 
    return -1

assert search([6,7,1,2,3,4,5], 2) == 3
assert search([10,11,12,13,1,2,3], 12) == 2
print('all tests have passed!')