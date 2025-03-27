def jump(nums):
    n = len(nums)
    if n == 1:
        return 0
    
    max_reach, steps, end = 0, 0, 0
    
    for i in range(n - 1):
        max_reach = max(max_reach, i + nums[i])
        if i == end:
            steps += 1
            end = max_reach
            if end >= n - 1:
                break
    
    return steps
nums = [2,3,1,1,4]
print(jump(nums))  
