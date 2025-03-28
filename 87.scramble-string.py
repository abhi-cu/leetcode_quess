def are_permutations(s1, s2):
    if len(s1) != len(s2):
        return False

    return sorted(s1) == sorted(s2)
s1 = "abcde"
s2 = "caebd"
output = are_permutations(s1, s2)
print(output)  