This pattern is based on the Breadth First Search (BFS) technique to traverse a tree.

Any problem involving the traversal of a tree in a level-by-level order can be efficiently solved using this approach. We will use a Queue to keep track of all the nodes of a level before we jump onto the next level. This also means that the space complexity of the algorithm will be O(W)O(W), where W is the maximum number of nodes on any level.


3 Queues
1. Result - append shows tree top to bottom, appendleft shows bottom to top
2. Current Level - append shows left to right, appendleft shows right to left
3. queue - always add append and popleft