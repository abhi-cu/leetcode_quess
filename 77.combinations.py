from itertools import combinations

def combine(n, k):
    return list(map(list, combinations(range(1, n + 1), k)))

n = 4
k = 2
print(combine(n, k))
