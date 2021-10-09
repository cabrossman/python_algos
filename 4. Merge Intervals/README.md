This pattern describes an efficient technique to deal with overlapping intervals. 

In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Given two intervals ('a' and 'b'), there will be six different ways the two intervals can relate to each other:
1. They dont overlap, A ends before B starts
2. They overlap. A occurs before. B ends after A
3. A completely overlaps B
4. They overlap. B occurs before. A ends after B.
5. B completely overlaps A
6. They dont overlap, B ends before A starts