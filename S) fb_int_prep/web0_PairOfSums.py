"""
https://www.metacareers.com/profile/coding_practice_question/?problem_id=840934449713537&c=793260865628340&psid=275492097255885&practice_plan=0&b=0222022
Pair Sums
Given a list of n integers arr[0..(n-1)], determine the number of different pairs of elements within it which sum to k.
If an integer appears in the list multiple times, each copy is considered to be different; that is, two pairs are considered different if one pair includes at least one array index which the other doesn't, even if they include the same values.
Signature
int numberOfWays(int[] arr, int k)
Input
n is in the range [1, 100,000].
Each value arr[i] is in the range [1, 1,000,000,000].
k is in the range [1, 1,000,000,000].
Output
Return the number of different pairs of elements which sum to k.
Example 1
n = 5
k = 6
arr = [1, 2, 3, 4, 3]
output = 2
The valid pairs are 2+4 and 3+3.
Example 2
n = 5
k = 6
arr = [1, 5, 3, 3, 3]
output = 4
There's one valid pair 1+5, and three different valid pairs 3+3 (the 3rd and 4th elements, 3rd and 5th elements, and 4th and 5th elements).
"""


def pairofsums_dups(arr, k):
    freq = {}# Step 1: Initialize a dictionary freq
    for num in arr: # Step 2: Populate freq
        freq[num] = freq.get(num, 0) + 1
    
    # Step 3: Count the pairs
    count = 0
    for x in list(freq.keys()): # use list to avoid RuntimeError because we're modifying the dictionary
        if k-x != x and k-x in freq:
            count += freq[x] * freq[k-x]
            del freq[k-x] # remove k-x to avoid counting the same pair again
            del freq[x]   # remove x as well
        elif k-x == x:
            count += freq[x]*(freq[x]-1)//2
            del freq[x]   # remove x after counting
    
    # Step 5: Return count
    return count


assert pairofsums_dups([1, 2, 3, 4, 3], 6) == 2
assert pairofsums_dups([1, 5, 3, 3, 3], 6) == 4