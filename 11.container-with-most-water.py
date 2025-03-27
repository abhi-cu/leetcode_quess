def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        h = min(height[left], height[right])
        w = right - left
        max_area = max(max_area, h * w)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height)) 
