def remove_duplicates(nums):
    if not nums:
        return 0
    
    index = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[index] = nums[i]
            index += 1
    
    return index

nums = [1, 1, 2]
k = remove_duplicates(nums)
print(k, nums[:k] + ['_'] * (len(nums) - k))  
