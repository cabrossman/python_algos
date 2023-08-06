# Next time
- DFS
- Subsets


# PRACTICE 

### Sliding window - O(N)
- fixed window size throughout
- right pointer is iterated through list and left pointer catches up in while loop
- O(N) complexity

### Two Pointers (3P) - O(N) - sorting N log N
- assumes sorted array
- left and right pointer come to middle. if target > test then left += 1 else right -=1
- O(N) complexity -- N log N for sorting

### Fast & Slow pointers O(N)
- has_cycle = slow & fast - when they meet TRUE
- cycle_len = at point of has_cycle. Keep one node fixed and iterate another
- cycle_start
    - p2 go into cycle => head++ cycle_len times
    - iterate p1 and p2 until meet


### Merge Intervals O(N) - sorting N log N
- NO OVERALP : A.end < B.start OR B.end < A.start
- sort by starts***
- Merge Overlaps
    - if overlap extend A.end = max(A.end, B.end)
    - if no overlap add A to list and make A = B. After loop add A
- Intersection of Two Lists
    - sort both
    - do while BOTH reaches end
    - if overlap - take intersection of overalp and add to list
    - if no overlap dont add
    - increment whichever list has longer end. If same iter both

### Cycle Sort - O(~2N)
- find duplicates or missing number
- put number in correct space

### Inplace Reverse Linked LIst - O(N)
- return prev
- reverse subLL
    - iterate until part to swap, cur and prev. Store these for later
    - swap
    - hook up (p_prev.next = prev) & (p_curr.next = curr)

### Breadth First Search - O(V + E)
- show level, invert binary tree, 
- return Top to Bottom, left to right of tree

### Depth First Search - O(V + E)
- terminal path is at leaf and other condition

### Two Heaps - O(log N)
- keep track in stream
- if odd add to one heap consistantly more
- the heads will be the middle number or numbers

### Subset - O(N * 2^N)
Subsets, All distinct elements (list of sets) event lists with dups
Permutations & string permutations (w/case)

### Modified Binary Search O(log N)

### K largest - N log K

### K way merge - N log K

### Typological sort O(E + V)
- relative order - many solutions
- build parent - child graph -> {i : []}, in_graph -> {i : cnt}
- sources -> vers with 0 in
- while sources -> pop left, add to list, dec in from all children. If child source add