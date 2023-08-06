"""
Given N ropes with different lengths, 
we need to connect these ropes into one big rope with minimum cost. 
The cost of connecting two ropes is equal to the sum of their lengths.

Input: [1, 3, 11, 5]
Output: 33
Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

Input: [3, 4, 5, 6]s
Output: 36
Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)



O(K * log K + (N−K) * log K) = O(N log K)
"""

from heapq import heappush, heappop

def minimum_cost_to_connect_ropes(ropes):
    min_heap = []
    for rope in ropes:
        heappush(min_heap, rope)

    tot = 0
    while min_heap:
        r1 = heappop(min_heap)
        r2 = heappop(min_heap)
        tot = tot + r1 + r2
        heappush(min_heap, r1 + r2)
        if len(min_heap) == 1:
            return tot
    return tot


assert minimum_cost_to_connect_ropes([1, 3, 11, 5]) == 33
assert minimum_cost_to_connect_ropes([3, 4, 5, 6]) == 36
assert minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]) == 42
print('all tests have passed!')
