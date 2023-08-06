# 10. Subsets

## What is it?
Permutations and Combinations of a given set of elements. This pattern describes an efficient Breadth First Search (BFS) approach to handle all these problems.

time complexity : 

## Why use it?
- Subsets, All distinct elements (list of sets) event lists with dups
- Permutations & string permutations (w/case)

## Concepts
- Breadth First Search
- If given duplicates sort first
- each iteration (with a new number) doubles the prior by adding a new combination.
- Algo is add empty set append previous sets and new number to double sets. Repeat
- If duplicate skip up to unique parts
- for permutations add last number to all positions

## Complexity - Generally
Subests
- Time Complexity: O(N * 2^N) or O(K^N * K)
- Auxiliary Space: O(N) or O(N * K)
Permutations
- Time Complexity: O(N!)
- Auxiliary Space: O(N)

## API
```
find_subsets(nums)
```

## How its done
### Distinct Subsets
```
def find_subsets(nums):
  subsets = [[]]
  for num in nums:
    for i in range(len(subsets)):
      subset = list(subsets[i])
      subset.append(num)
      subsets.append(subset)
  return subsets
```

## Variants
### Duplicates
```
def find_subsets(nums):
  nums.sort()
  subsets = [[]]
  start, end = 0,0
  for i in range(len(nums)):
    start = 0
    if i > 0 and nums[i] == nums[i-1]:
      start = end
    end = len(subsets)
    for j in range(start, end):
      subset = list(subsets[j])
      subset.append(nums[i])
      subsets.append(subset)
  return subsets
```
### Permutations
```
def find_permutations(nums):
    result = []
    permutations = deque()
    permutations.append([])
    for i in range(len(nums)): # on the last iteration everything is added to result
        for _ in range(len(permutations)): #later we add to permutation
            # we pop to mutate the list in the deque
            permutation_A = permutations.popleft() #this saves the n-1 version to add to list later
            #need one more than n which only has 2 in the example to get all permutations
            for j in range(len(permutation_A) + 1): 
                permutation_B = list(permutation_A)
                permutation_B.insert(j, nums[i]) #we insert the nth number at each possible position
                if len(permutation_B) == len(nums): ### must have all numbers and add to result
                    result.append(permutation_B)
                else:
                    permutations.append(permutation_B) ###intermediatery
    return result

```