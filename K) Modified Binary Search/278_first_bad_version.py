"""First Bad Version

given a list of bad versions return the index of the first one

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
"""

def badv(versions, isBadVersion):
    left, right = 0, versions
    while left < right:
        mid = (right - left)//2 + left
        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left if isBadVersion(left) else -1


isBadVersion = lambda version: version >= 1
assert badv(1,isBadVersion) == 1

isBadVersion = lambda version: version >= 6
assert badv(5,isBadVersion) == -1

isBadVersion = lambda version: version >= 1
assert badv(5,isBadVersion) == 1

isBadVersion = lambda version: version >= 4
assert badv(7,isBadVersion) == 4
print('all tests passed!')

