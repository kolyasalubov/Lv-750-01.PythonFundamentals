# array1 = [True,  True,  True,  False,
#                   True,  True,  True,  True ,
#                   True,  False, True,  False,
#                   True,  False, False, True ,
#                   True,  True,  True,  True ,
#                   False, False, True,  True ];

def count_sheeps(sheep):
    """ Count sheeps func"""
    total = 0
    for value in sheep:
        if value == True:
            total += 1
    return total