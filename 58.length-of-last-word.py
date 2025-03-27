def length_of_last_word(s):
    return len(s.strip().split()[-1])
s = " fly me to the moon "
print(length_of_last_word(s))  
