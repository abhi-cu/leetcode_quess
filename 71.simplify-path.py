def simplify_path(path):
    stack = []
    parts = path.split("/")

    for part in parts:
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)

    return "/" + "/".join(stack)

path = "/home/"
print(simplify_path(path)) 
