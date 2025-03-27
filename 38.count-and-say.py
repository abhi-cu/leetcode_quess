def count_and_say(n):
    if n == 1:
        return "1"
    
    prev = count_and_say(n - 1)
    result = ""
    count = 1
    
    for i in range(len(prev)):
        if i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
        else:
            result += str(count) + prev[i]
            count = 1
    
    return result

n = 4
print(count_and_say(n))  
