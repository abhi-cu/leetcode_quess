def three_sum_closest(nums, target):
    nums.sort()
    closest_sum = float('inf')
    
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if abs(target - total) < abs(target - closest_sum):
                closest_sum = total
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total
    
    return closest_sum

nums = [-1,2,1,-4]
target = 1
print(three_sum_closest(nums, target))  
