from itertools import combinations

def subsets(nums):
    result = [[]]
    for i in range(1, len(nums) + 1):
        result.extend([list(comb) for comb in combinations(nums, i)])
    return result

nums = [1, 2, 3]
print(subsets(nums))
