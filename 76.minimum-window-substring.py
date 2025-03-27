from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window_count = {}
    left, right = 0, 0
    required = len(t_count)
    formed = 0
    min_length = float("inf")
    min_window_substr = ""

    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                min_window_substr = s[left:right + 1]

            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed -= 1

            left += 1

        right += 1

    return min_window_substr

s = "ADOBECODEBANC"
t = "ABC"
print(min_window(s, t))
