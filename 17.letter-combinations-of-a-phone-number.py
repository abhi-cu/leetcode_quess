from itertools import product

def letter_combinations(digits):
    if not digits:
        return []
    
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    char_lists = [phone_map[d] for d in digits]
    return ["".join(comb) for comb in product(*char_lists)]

digits = "23"
print(letter_combinations(digits)) 
