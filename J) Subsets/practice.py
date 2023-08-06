from collections import deque
def find_subsets(nums):
  # create a list that contains empty list as the subsets container
  # iterate over each number in the list given
  # at each iteration grab every element in the subsets container and create a new subset 
  # that adds the current number to each element creating new subsets and appending to the list
  subsets = [[]]
  for num in nums:
    for i in range(len(subsets)):
      subset = list(subsets[i])
      subset.append(num)
      subsets.append(subset)
  return subsets

def find_subsets_dups(nums):
  # assumes sorted list
  # create subset container
  # create pointers for start and end to determine 
  ## which subsets need to be added depending on the dups
  # iterate over nums
  ## check for dups (current num = last num)
  ### if dups found make start = end
  #### end usually denotes the length of the subset at the last iteration
  #### this sets the adding subsets to the point of the start of last iterations
  # return subsets
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

def find_permutations(nums):
  #create container for result and intermediate perms
  # iterate over list of nums
  ## iterate over current length of perms - pop first element called subset
  ### iterate over length of subset + 1 to insert existing num at all possible positions
  ### if current subset length after insertion is equal to num list then insert to result
  ### otherwise insert to perm list
  # return result
  result = []
  perms = deque()
  perms.append([])
  for i in range(len(nums)):
    for _ in range(len(perms)):
      subset = perms.popleft()
      for j in range(len(subset)+1):
        sub_copy = list(subset)
        sub_copy.insert(j, nums[i])
        if len(sub_copy) == len(nums):
          result.append(sub_copy)
        else:
          perms.append(sub_copy)
  return result

  # create a list for the permutations and add the string
  # iterate of the length of the string - i
  ## check if string element is a number - if so nothing to do - continue
  ## iterate over current list of permuations
  ### switch the case of letter i and add it to the perm list
  # return perm list
  permutations = [s]
  for i in range(len(s)):
      if s[i].isnumeric():
          continue
      for j in range(len(permutations)):
          perm = list(permutations[j])
          perm[i] = perm[i].swapcase()
          permutations.append(''.join(perm))
  return permutations

def find_letter_case_string_permutations(s):
  # create a list for the permutations and add the string
  # iterate of the length of the string - i
  ## check if string element is a number - if so nothing to do - continue
  ## iterate over current list of permuations
  ### switch the case of letter i and add it to the perm list
  # return perm list
  perms = [s]
  for i in range(len(s)):
    if s[i].isnumeric():
      continue
    for j in range(len(perms)):
      perm = list(perms[j])
      perm[i] = perm[i].swapcase()
      perms.append(''.join(perm))
  return perms

assert find_subsets([1, 3]) == [[], [1], [3], [1, 3]]
assert find_subsets([1, 5, 3]) == [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]

assert find_subsets_dups([1, 3, 3]) == [[], [1], [3], [1,3], [3,3], [1,3,3]]
assert find_subsets_dups([1, 5, 3, 3]) == [
  [], [1], [3], [1,3],[3,3], [1,3,3], [5], [1,5], [3,5], [1,3,5], [3,3,5], [1,3,3,5]
]

assert find_permutations([1, 3, 5]) == [
    [5,3,1],
    [3,5,1],
    [3,1,5],
    [5,1,3],
    [1,5,3],
    [1,3,5]
]

assert find_letter_case_string_permutations("ad52") == [
    "ad52", "Ad52", "aD52", "AD52"
]
assert find_letter_case_string_permutations("ab7c") == [
    "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"
]

print("all tests have passed!")