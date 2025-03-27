def combination_sum2(candidates, target):
    def backtrack(start, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        
        prev = -1
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            if candidates[i] == prev:
                continue
            path.append(candidates[i])
            backtrack(i + 1, target - candidates[i], path, res)
            path.pop()
            prev = candidates[i]
    
    result = []
    candidates.sort()
    backtrack(0, target, [], result)
    return result

candidates = [10,1,2,7,6,1,5]
target = 8
print(combination_sum2(candidates, target))  
