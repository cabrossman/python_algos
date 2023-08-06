def find_sum_of_three(nums, target):
    nums.sort()
    for idx in range(len(nums)):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            zsum = nums[idx] + nums[left] + nums[right]
            if zsum == target:
                return True
            if target > zsum:
                left += 1
            elif target < zsum:
                right -= 1
            else:
                left += 1
    return False

assert find_sum_of_three([-1,2,1,-4,5,-3], -8) == True
assert find_sum_of_three([1,-1,0],-1) == True
#assert find_sum_of_three([3,7,1,2,8,4,5], 10) == 
#assert find_sum_of_three([3,7,1,2,8,4,5], 21) == 


