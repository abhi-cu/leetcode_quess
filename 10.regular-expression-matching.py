import re

def is_match(s, p):
    return re.fullmatch(p, s) is not None
s = "aa"
p = "a"
print(is_match(s, p)) 