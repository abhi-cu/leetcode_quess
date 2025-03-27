from itertools import permutations

def permute_unique(nums):
    return list(map(list, set(permutations(nums))))
nums = [1,1,2]
print(permute_unique(nums))  
