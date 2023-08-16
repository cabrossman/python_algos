"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
"""


from collections import defaultdict, deque

def findCheapestPrice(n, flights, src, dst, k):
    # Construct the graph
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    # BFS queue [(city, cost, stops)]
    queue = deque([(src, 0, 0)])
    min_price = float('inf')

    while queue:
        city, cost, stops = queue.popleft()

        # If the current city is the destination
        if city == dst:
            min_price = min(min_price, cost)
            continue

        # If the number of stops is within the limit, explore neighbors
        if stops <= k:
            for neighbor, price in graph[city]:
                if cost + price < min_price:  # Pruning step
                    queue.append((neighbor, cost + price, stops + 1))

    # If the destination city was not reached or exceeds the limit, return -1
    return min_price if min_price != float('inf') else -1