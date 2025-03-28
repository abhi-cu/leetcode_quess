def restore_ip_addresses(s):
    def backtrack(start, path):
        if start == len(s) and len(path) == 4:
            res.append(".".join(path))
            return
        if len(path) >= 4:
            return
        
        for step in range(1, 4):
            part = s[start:start + step]
            if not part:
                continue
            if (len(part) > 1 and part[0] == "0") or int(part) > 255:
                continue
            backtrack(start + step, path + [part])
    
    res = []
    backtrack(0, [])
    return res

s = "25525511135"
print(restore_ip_addresses(s))
