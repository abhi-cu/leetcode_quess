import math

def get_permutation(n, k):
    numbers = list(range(1, n + 1))
    k -= 1  
    result = []

    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        index = k // fact
        result.append(str(numbers.pop(index)))
        k %= fact

    return "".join(result)

n = 3
k = 3
print(get_permutation(n, k))  
