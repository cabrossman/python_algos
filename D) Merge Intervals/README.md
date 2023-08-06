# 4. Merge Intervals

## What is it?
This pattern describes an efficient technique to deal with overlapping intervals. In a lot of problems involving intervals, we either need to find overlapping intervals or merge intervals if they overlap.

Time Complexity : O(N*log(N)) for sorting & O(N) for merging intervals

## Why use it?
- Merge Intervals
- Insert Intervals
- Given two lists of intervals, find the intersection of these two lists. 
- Given an array of intervals representing 'N' appointments, find out if a person can attend all the appointments.


## Concepts
1. First Sort the intervals
2. Ways define overlap
    ```
    Given two intervals ('a' and 'b'), there will be six different ways the two intervals can relate to each other:
    1. They dont overlap, A ends before B starts
    2. They overlap. A occurs before. B ends after A
    3. A completely overlaps B
    4. They overlap. B occurs before. A ends after B.
    5. B completely overlaps A
    6. They dont overlap, B ends before A starts
    ```
3. Another way to say overlap
  ```
      NOT OVERLAP
      1. Aend < Bstart
      2. Bend < Astart

      OVERLAP
      1. Aend <= Bstart and Astart <= Bstart #B starts a bit later than A
      2. Bstart >= Astart & Bend <= Aend #B inside A
      3. Bend <= Astart and Bstart <= Astart #A starts a bit later than B
      4. Astart >= Bstart & Aend <= Bend #A inside B
  ```

## Complexity - Generally
time complexity : O(N*log(N)) for sorting & O(N) for merging intervals
space complexity : O(N) for list, but auxilary is O(1) - doesnt store values

## API
```
merge(intervals) #to merge itself
merge(intervalsA, intervalsB) # to merge two lists
```

## How its done
### Basic Algo to merge existing interavals together
Always remember to sort the interval based on START
```
def merge(intervals):
  merged = []
  intervals.sort(key = lambda x: x[0])
  if len(intervals) < 2:
      return intervals
  Astart, Aend = intervals.pop(0)
  for Bstart, Bend in intervals:
      if Bstart <= Aend: #overlap, extend the end
         Aend = max(Aend,Bend) 
      else: #some overlap
        merged.append([Astart, Aend])
        Astart, Aend = Bstart, Bend
  merged.append([Astart, Aend])
  return merged
```
### Insert Interval - find intersection
1. Loop while counters are less then interval len
2. If overlap - take max of start and min of end and append to merged list
3. Increment counters - if B.end < A.end Inc b else Inc A
```
def merge(intervalsA, intervalsB):
  merged = []
  a,b = 0,0
  while b < len(intervalsB) and a < len(intervalsA):
    #no overlap
    if intervalsA[a].end < intervalsB[b].start or intervalsB[b].end < intervalsA[a].start:
      pass
    else:
      start = max(intervalsA[a].start, intervalsB[b].start)
      end = min(intervalsA[a].end, intervalsB[b].end)
      merged.append(Interval([start,end]))
  
    if intervalsB[b].end == intervalsA[a].end:
      a = a + 1
      b = b + 1
    elif intervalsB[b].end < intervalsA[a].end:
      b = b + 1
    else: # A.end is smaller
      a = a + 1
  return interval_to_list(merged)
```