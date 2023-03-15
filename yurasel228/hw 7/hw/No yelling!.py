def filter_words(s):
    words = s.split()
    words[0] = words[0][0].upper() + words[0][1:].lower()
    for i in range(1, len(words)):
        words[i] = words[i].lower()
    return ' '.join(words)
print(filter_words('HELLO CAN YOU HEAR ME'))