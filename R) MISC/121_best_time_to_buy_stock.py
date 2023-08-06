"""
You are given an array of prices where prices[i] 
is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
profit = 6-1 = 5.

"""

def max_prof(arr):
    max_prof = 0
    if len(arr) <= 1:
        return max_prof
    left, right = 0, 1
    
    while right <= len(arr) - 1:
        if arr[left] >= arr[right]:
            left = right
            right += 1
        else:
            curr_prof = arr[right] - arr[left]
            max_prof = max(max_prof,curr_prof)
            right += 1
    return max_prof

assert max_prof([7,1,5,3,6,4]) == 5
assert max_prof([7,6,4,3,1]) == 0
assert max_prof([1,2,3,4,5]) == 4
assert max_prof([4]) == 0
assert max_prof([2,4,1]) == 2
print('all tests have passed!')