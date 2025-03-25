def longest_palindromic_substring(s):
    if not s:
        return ""
    start, max_length = 0, 0
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1
    for i in range(len(s)):
        l1, r1 = expand_around_center(i, i)
        l2, r2 = expand_around_center(i, i + 1)
        if r1 - l1 > max_length:
            start, max_length = l1, r1 - l1
        if r2 - l2 > max_length:
            start, max_length = l2, r2 - l2
    return s[start:start + max_length + 1]
s = "babad"
print(longest_palindromic_substring(s)) 