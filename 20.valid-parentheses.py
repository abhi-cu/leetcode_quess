def is_valid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if top_element != bracket_map[char]:
                return False
        else:
            stack.append(char)
    
    return not stack
s = "()[]{}"
print(is_valid(s)) 
