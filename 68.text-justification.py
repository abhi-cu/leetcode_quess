def full_justify(words, maxWidth):
    res, cur, num_of_letters = [], [], 0

    for word in words:
        if num_of_letters + len(word) + len(cur) > maxWidth:
            for i in range(maxWidth - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += " "
            res.append("".join(cur))
            cur, num_of_letters = [], 0
        cur.append(word)
        num_of_letters += len(word)

    res.append(" ".join(cur).ljust(maxWidth))
    return res

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
output = full_justify(words, maxWidth)

for line in output:
    print(f'"{line}"')
