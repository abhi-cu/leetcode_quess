def total_n_queens(n):
    def backtrack(row, diagonals, anti_diagonals, cols):
        if row == n:
            nonlocal count
            count += 1
            return
        
        for col in range(n):
            curr_diagonal = row - col
            curr_anti_diagonal = row + col
            
            if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                continue
            
            cols.add(col)
            diagonals.add(curr_diagonal)
            anti_diagonals.add(curr_anti_diagonal)
            
            backtrack(row + 1, diagonals, anti_diagonals, cols)
            
            cols.remove(col)
            diagonals.remove(curr_diagonal)
            anti_diagonals.remove(curr_anti_diagonal)
    
    count = 0
    backtrack(0, set(), set(), set())
    return count
n = 4
print(total_n_queens(n)) 
