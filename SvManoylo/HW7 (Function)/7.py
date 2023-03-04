# spisok = [10, 40, 20, 30]
# i = 0
# while i < len(spisok):
#     spisok[i] = spisok[i] + 2  
#     i = i + 1
# print(spisok)


def add_indexes(lst):
    index = enumerate(lst)
    i = 0
    while i < len(lst):
        lst[i] = lst[i] + index[i]
        i = i + 1
    return lst 

    
lst = (2, 5, 6)
x = add_indexes(lst)
print(x)