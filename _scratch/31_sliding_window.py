def main(l,s):
    start = 0 #start at 0
    running_tot = 0 #start at 0
    smallest_sub_arry = len(l) #smallest is whole list
    for end in range(len(l)): #iterate through list
        running_tot += l[end]
        while running_tot >= s: #if passed threshold
            smallest_sub_arry = min(smallest_sub_arry, end - start + 1)
            running_tot -= l[start]
            start += 1
    return smallest_sub_arry
        


assert main([2, 1, 5, 2, 3, 2],7) == 2
assert main([2, 1, 5, 2, 8], 7) == 1
assert main([3, 4, 1, 1, 6], 8) == 3

print('all tests past!')
