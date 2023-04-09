def count_characters(w):
    counts = {}
    for item in w:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


print(count_characters("hello"))