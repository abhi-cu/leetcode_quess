from collections import Counter

def find_substring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count
    word_map = Counter(words)
    result = []
    
    for i in range(len(s) - total_len + 1):
        seen = Counter()
        for j in range(word_count):
            word_index = i + j * word_len
            word = s[word_index:word_index + word_len]
            if word in word_map:
                seen[word] += 1
                if seen[word] > word_map[word]:
                    break
            else:
                break
        else:
            result.append(i)
    
    return result
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(find_substring(s, words)) 
