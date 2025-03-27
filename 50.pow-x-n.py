def my_pow(x, n):
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n
    
    result = 1.0
    while n:
        if n % 2:
            result *= x
        x *= x
        n //= 2
    return result
x = 2.00000
n = 10
print(my_pow(x, n))  
