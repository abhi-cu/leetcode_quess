def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    rows = ["" for _ in range(numRows)]
    index, step = 0, 1
    for char in s:
        rows[index] += char
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
    return "".join(rows)
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows))