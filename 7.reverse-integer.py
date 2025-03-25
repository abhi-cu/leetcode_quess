def reverse_integer(x):
    sign = -1 if x < 0 else 1
    reversed_num = int(str(abs(x))[::-1]) * sign
    if reversed_num < -2**31 or reversed_num > 2**31 - 1:
        return 0
    return reversed_num
x = 123
print(reverse_integer(x))