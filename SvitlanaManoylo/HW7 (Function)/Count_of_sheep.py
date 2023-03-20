def count_sheeps(sheep):
    count = 0
    if sheep is None:
        return count
    for s in sheep:
        if s:
            count += 1
    return count