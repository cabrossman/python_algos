"""
Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6
"""

class SparseVector:
    def __init__(self, nums):
        self.nums = {i: v for i, v in enumerate(nums) if v != 0}

    def dotProduct(self, vec):
        if len(self.nums) > len(vec.nums):
            return vec.dotProduct(self)

        return sum(v * vec.nums.get(i, 0) for i, v in self.nums.items())

def dot(nums1, nums2):
    tot = 0
    for num1, num2 in zip(nums1, nums2):
        tot += num1*num2
    return tot

assert dot(nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]) == 8
assert dot(nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]) == 0
assert dot(nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]) == 6
print('all tests passed')