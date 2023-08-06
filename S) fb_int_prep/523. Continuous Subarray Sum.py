"""
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
"""

def good_subarray(nums, k):
    prefix = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        prefix[i+1] = prefix[i] + nums[i]
    """
    Let's suppose that the remainder mod was first encountered at index j 
    and now again at index i (where i > j). The sum of the elements 
    between j+1 and i (both inclusive) will be prefix[i] - prefix[j], 
    and importantly, this sum will be a multiple of k!
    This is because the remainder when prefix[i] is divided by k 
    is the same as when prefix[j] is divided by k - 
    this implies that the difference between prefix[i] and prefix[j] 
    is divisible by k.
    """
    hashmap = {0: -1}
    for i in range(1, len(nums) + 1):
        mod = prefix[i] % k
        if mod in hashmap:
            prefix_i = hashmap[mod]
            #needs to be more than 2 since
            # prefix has 1 more than nums index
            if i - prefix_i > 1: 
                return True
        else:
            hashmap[mod] = i
    return False

assert good_subarray(nums = [23,2,4,6,7], k = 6) == True
assert good_subarray(nums = [23,2,6,4,7], k = 6) == True
print('all tests passed!')