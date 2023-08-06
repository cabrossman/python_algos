from heapq import heappush, heappop

def find_k_largest_numbers(nums, k):
  # iterate through nums
  # put first k in min heap
  # for rest of list just check its bigger than the smallest
  ## number in min_heap. If so pop that and push in num - else skip
  min_heap = []
  for i, num in enumerate(nums):
    if i < k:
      heappush(min_heap, num)
    elif num > min_heap[0]:
      heappop(min_heap)
      heappush(min_heap, num)
  return sorted(list(min_heap))

def find_kth_smallest_numbers(nums, k):
  # to find smallest - reverse direction of heap by multiplying each num by -1
  # this will return the lagest int value (which is negative)

  ## iterate through list - add to heap k items
  ## next check if that item is larger than current head of heap
  ### if so pop and push

  max_heap = []
  for i, num in enumerate(nums):
    if i < k:
      heappush(max_heap, -num)
    elif num < -max_heap[0]:
      heappop(max_heap)
      heappush(max_heap, -num)
  return -max_heap[0]

def find_k_freq_nums(nums, k):
  # create map num : count
  # iterate over keys adding to heap (val, key)
  ## when len(min_heap) > k - start poping so you are left
  ### k most frequent numbers
  counter = {}
  for num in nums:
    counter[num] = counter.get(num,0) + 1

  min_heap = []
  for num, count in counter.items():
    heappush(min_heap, (count,num))
    if len(min_heap) > k:
      heappop(min_heap)

  return sorted([l[1] for l in list(min_heap)])

def find_k_frequent_letters(letters):

    ### map counter
    m = {}
    for letter in letters:
        m[letter] = m.get(letter,0) + 1

    ## heap to find k largest
    max_heap = []
    for letter, count in m.items():
        heappush(max_heap, (-count, letter))

    sorted_letters = []
    for _ in list(max_heap):
        letter = heappop(max_heap)
        for _ in range(abs(letter[0])):
            sorted_letters.append(letter[1])

    return ''.join(sorted_letters)

def find_closest_elements(nums, K, X):
    #store tuple of (dist, num) in min_heap
    max_heap = []
    for i, num in enumerate(nums):
        dist_num_tuple = (-abs(num - X), num)
        heappush(max_heap, dist_num_tuple)
        if i >= K:
          heappop(max_heap)
    return sorted([dist_tuple[1] for dist_tuple in max_heap])

assert find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3) == [5, 11, 12]
assert find_k_largest_numbers([5, 12, 11, -1, 12], 3) == [11, 12, 12]
assert find_k_largest_numbers([100, 100, 2, 50, 49], 3) == [50, 100, 100]

assert find_kth_smallest_numbers([1, 5, 12, 2, 11, 5], k = 3) == 5
assert find_kth_smallest_numbers([1, 5, 12, 2, 11, 5], k = 4) == 5
assert find_kth_smallest_numbers([5, 12, 11, -1, 12], k = 3) == 11

assert find_k_freq_nums([1, 3, 5, 12, 11, 12, 11], k = 2) == [11, 12]
assert find_k_freq_nums([5, 12, 11, 3, 11], k = 2) in [[5,11], [11, 12], [3, 11]]

assert find_k_frequent_letters('Programming') == 'ggmmrrPaino'
assert find_k_frequent_letters('abcbab') == 'bbbaac'

assert find_closest_elements([5, 6, 7, 8, 9], 3, 7) == [6, 7, 8]
assert find_closest_elements([2, 4, 5, 6, 9], 3, 6) == [4, 5, 6]
assert find_closest_elements([2, 4, 5, 6, 9], 3, 10) == [5, 6, 9]
print('all tests have passed!')