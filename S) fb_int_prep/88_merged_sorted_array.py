"""
You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, 
and two integers m and n, representing the number of 
elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, 
but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. 
nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""
def merge(nums1, m, nums2, n):
    # go backwards in array selecting the largest number in
    # first array. Create two pointers for valid numbers and
    # an overall pointer for the whole array
    #INFORMATION THAT BOTH ARE SORTED IS IMPORTANT
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1 # Pointer for current position in merged array
    # While there are still elements to compare in both arrays
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # If there are still elements in nums2
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1

nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3
output=[1,2,2,3,5,6]
assert merge(nums1, m, nums2, n) == output

nums1=[0]
m=0
nums2=[1]
n=1
output=[1]
assert merge(nums1, m, nums2, n) == output

nums1=[2,2,2,0,0,0]
m=3
nums2=[2,2,2]
n=3
output=[2,2,2,2,2,2]
assert merge(nums1, m, nums2, n) == output

nums1=[-4,-2,0,0,0]
m=2
nums2=[-3,-1,5]
n=3
output=[-4,-3,-2,-1,5]
assert merge(nums1, m, nums2, n) == output

nums1=[1,1,1,0,0,0]
m=3
nums2=[1,1,1]
n=3
output=[1,1,1,1,1,1]
assert merge(nums1, m, nums2, n) == output

nums1=[4]
m=1
nums2=[]
n=0
output=[4]
assert merge(nums1, m, nums2, n) == output

nums1=[1,3,5,7,0,0,0,0,0]
m=4
nums2=[2,4,6,8,10]
n=5
output=[1,2,3,4,5,6,7,8,10]
assert merge(nums1, m, nums2, n) == output
print('all tests passed!')