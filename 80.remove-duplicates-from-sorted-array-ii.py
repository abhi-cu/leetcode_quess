def remove_duplicates(nums):
    if not nums:
        return 0

    k = 0  # Pointer for the position to overwrite
    for num in nums:
        if k < 2 or num != nums[k - 2]:
            nums[k] = num
            k += 1

    return k

nums = [1,1,1,2,2,3]
k = remove_duplicates(nums)
print(k, nums[:k] + ["_"] * (len(nums) - k))
