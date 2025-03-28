def subsets_with_dup(nums):
    nums.sort()
    res = [[]]
    start_idx = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            start_idx = size
        else:
            start_idx = 0
        size = len(res)
        for j in range(start_idx, size):
            res.append(res[j] + [nums[i]])
    return res

nums = [1,2,2]
print(subsets_with_dup(nums))
