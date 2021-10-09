def max_sub_array_of_size_k(k, arr):
  window_sum, highest_window = 0,0
  k = k - 1
  for i in range(len(arr)):
    window_sum = window_sum + arr[i]
    print(i, window_sum)
    if i < k:
      continue
    if window_sum > highest_window:
      highest_window = window_sum
    window_sum = window_sum - arr[i-k]
  return highest_window


print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))