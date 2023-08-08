"""Given an array nums of n integers where n > 1,  
return an array output such that output[i] is equal 
to the product of all the elements of nums except nums[i]."""

def product_except(arr):
    tot_product = 1
    for n in arr:
        tot_product = tot_product * n
    #same as sum - n... but multiplication
    new_arr = [tot_product / n for n in arr]
    return new_arr

assert product_except([5,12,6]) == [72, 30, 60]
print('all tests have passed!')