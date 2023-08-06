"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Input: num = 9973
Output: 9973
Explanation: No swap.
"""
def max_swap(nums):
    #convert to String and list
    num_lst = list(str(nums))  #N
    #get last idx of each number - we'd prefer this higher
    last_oc_map = {num : i for i, num in enumerate(num_lst)} #N

    for i, num in enumerate(num_lst): #N
        for dig in range(9, int(num), -1): #any number greater than current num?
            if last_oc_map.get(dig): #if so then swap
                idx = last_oc_map.get(dig)
                num_lst[i], num_lst[idx] = num_lst[idx], num_lst[i]
                return int(''.join(num_lst))
    return int(''.join(num_lst))
    
assert max_swap(4321) == 4321
assert max_swap(2736) == 7236
assert max_swap(9973) == 9973