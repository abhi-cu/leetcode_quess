def search_range(nums, target):
    def find_left(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def find_right(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    left, right = find_left(nums, target), find_right(nums, target)
    return [left, right] if left <= right else [-1, -1]
nums = [5,7,7,8,8,10]
target = 8
print(search_range(nums, target))
