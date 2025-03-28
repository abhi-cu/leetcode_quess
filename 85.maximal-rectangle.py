def maximalRectangle(matrix):
    if not matrix:
        return 0

    def largestRectangleArea(heights):
        stack, max_area = [], 0
        heights.append(0)  
        
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        heights.pop()  
        return max_area

    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_rectangle = 0

    for row in matrix:
        for j in range(cols):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
        max_rectangle = max(max_rectangle, largestRectangleArea(heights))

    return max_rectangle

matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

print(maximalRectangle(matrix))  
