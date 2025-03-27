def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

a = "11"
b = "1"
print(add_binary(a, b))
