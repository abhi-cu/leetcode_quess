import re

def extract_number(s):
    match = re.search(r'\d+', s)
    return int(match.group()) if match else None


s = "1337c0d3"
print(extract_number(s)) 