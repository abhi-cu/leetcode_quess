def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

s = "0"
print(is_number(s))
