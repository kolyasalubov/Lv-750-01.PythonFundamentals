#while
############################

# i = 5
# while i <= 15:
#     print(i)
#     i = i + 2

##################
# for
##################


# for i in 'hello world':
#     print(i*2, end='№')
#     # print(i * 2)


#у вище вказаному прикладі функція print() має 
# також аргумент end — він вказує, яким символом 
# має закінчуватись поточне виведення на екран. 
# Якщо в функції print() не вказаний даний аргумент 
# то виведення закінчується символом переходу на 
# нову стрічку (\n).
#for
#
# spisok = [10, 40, 20, 30]
# for element in spisok:
#     print(element + 2)
# print(spisok)
# ##for

# spisok = [10, 40, 20, 30]
# i = 0
# for element in spisok:
#      spisok[i] = element + 2
#      i += 1
#      print(element)
# print(spisok)


######################
#for для dictionary
######################

# d = {1:'one',2:'two',3:'three',4:'four'}
# for key in d:
#     d[key] = d[key] + '#'

# print(d)

##############
###while
#################
# 
# spisok = [10, 40, 20, 30]
# i = 0
# while i < len(spisok):
#     spisok[i] = spisok[i] + 2  
#     i = i + 1
# print(spisok)

# ##############################
# # continue виходить з ітерації, починає наступну
# ################################################

# for i in 'hello world':
#     if i == 'o':
#         continue
#     print(i * 2, end='')

###############################
#break достроково перериває цикл
#####################################

# for i in 'hello world':
#     if i == 'o':
#         break
#     print(i * 2, end='')
    
    #Службове слово else, яке застосовується 
    # в циклі while чи for перевіряє чи був вихід 
    # з циклу з допомогою слова break, блок коду
    # після else буде виконаний лише у випадку 
    # якщо не спрацював break
    ############################### 
# for i in 'hello world':
#     if i == 'a':
#         break
# else:
#     print('The letter is missing from the line')
# print("OOps!!!")

#############################
#range
##############################
# a = range(-10, 10)
# print(type(a))
# print(a)
# print(list(a))
####################

# spisok = [10, 40, 20, 30]
# print(list(range(len(spisok))))
# print(range(len(spisok)))

#############################################
# range(0, 4) генерує послідовність від 0 до 3
#############################################

# spisok = [10, 40, 20, 30]
# for i in range(len(spisok)):
#     spisok[i] += 2
#     print(i,spisok[i])