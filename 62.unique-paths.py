def unique_paths(m, n):
    from math import comb
    return comb(m + n - 2, m - 1)

m = 3
n = 7
print(unique_paths(m, n))  
