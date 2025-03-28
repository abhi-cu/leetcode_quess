def gray_code(n):
    result = [0]
    for i in range(n):
        result += [x | (1 << i) for x in reversed(result)]
    return result

n = 2
print(gray_code(n))
