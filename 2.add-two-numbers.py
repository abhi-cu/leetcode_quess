def add(list1, list2):
    n1 = int("".join(map(str, list1[::-1])))
    n2 = int("".join(map(str, list2[::-1])))
    total = n1 + n2
    return [int(digit) for digit in str(total)][::-1]
l1 = [2, 4, 3]
l2 = [5, 6, 4]
print(add(l1, l2))  