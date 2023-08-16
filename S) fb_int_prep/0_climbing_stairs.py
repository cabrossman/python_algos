"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps


Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def main(n):

    """
    For any step i greater than 2, you can reach there either 
    from step i-1 or from step i-2. So, the total number of 
    ways to reach step i is the sum of the ways to 
    reach step i-1 and step i-2.

    ways[0] = 1
    ways[1] = 1
    ways[i] = ways[i-1] + ways[i-2] for i>1
    
    only need to keep track of current, prior & prior_prior
    """
    if n == 1: return 1
    if n == 2: return 2
    way_i_2, way_i_1 = 1, 2
    for _ in range(3, n + 1):
        new_way = way_i_2 + way_i_1
        way_i_1, way_i_2 = new_way, way_i_1
    return new_way

assert main(2) == 2 # 1 step + 1 Step OR 2 Steps
assert main(3) == 3 # 1 step 3 times, 1 step + 2 steps, 2 steps + 1 step
print(main(10))
print('all tests passed!')