def count_chars(s):
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count
s = "bababooi"
char_count = count_chars(s)
print(char_count)