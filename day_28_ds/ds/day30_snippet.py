def remove_mult_x(L, x): 
    assert type(L) is list and x is not None 
    new_L = list(filter((lambda num: num != x), L)) 
    return new_L 
    
print(remove_mult_x([1, 7, 2, 2, 4, 8, 2, 6], 2)    )

# > reticulate::source_python('C:/.../my_100_days/day30_snippet.py')
# [1, 7, 4, 8, 6]

# Useful if you want to remove all negative values from a list, or if you want to remove all 0's 
# you would amend lambda to have num < 0 as an example
