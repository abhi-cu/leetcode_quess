def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)
    
    return max_length
s = "(()"
print(longest_valid_parentheses(s))  
