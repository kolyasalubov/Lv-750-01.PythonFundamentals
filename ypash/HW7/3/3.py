def letter_caunter(word):
    d = {}
    for i in word:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d



print(letter_caunter("hello"))



