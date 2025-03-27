def combination_sum(candidates, target):
    def backtrack(start, target, path, res):
        if target == 0:
            res.append(path[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path, res)
            path.pop()
    
    result = []
    candidates.sort()
    backtrack(0, target, [], result)
    return result

candidates = [2,3,6,7]
target = 7
print(combination_sum(candidates, target))
