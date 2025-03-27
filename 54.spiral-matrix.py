def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # Take the first row
        if matrix and matrix[0]:  # Rotate the remaining matrix counter-clockwise
            matrix = list(zip(*matrix))[::-1]
    return result
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_order(matrix))  