def remove_element(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    
    return index
nums = [3,2,2,3]
val = 3
k = remove_element(nums, val)
print(k, nums[:k] + ['_'] * (len(nums) - k))
