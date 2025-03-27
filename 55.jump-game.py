def can_jump(nums):
    max_reach = 0
    for i, num in enumerate(nums):
        if i > max_reach:
            return False  # If we can't reach this index, return False
        max_reach = max(max_reach, i + num)  # Update the farthest index we can reach
        if max_reach >= len(nums) - 1:
            return True  # If we can reach the last index, return True
    return False
nums = [2, 3, 1, 1, 4]
print(can_jump(nums))  