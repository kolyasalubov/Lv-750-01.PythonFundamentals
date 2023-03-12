
# total = 0

# def my_sum(arg1, arg2):
    
#     global total 
#     total = arg1 + arg2
#     print("Inside the function total : ", total)
#     return total
    
# print("before", total)
# my_sum(56, 30)
# print("Outside the function total : ", total)


# def print_info(name, age = 18):
#     print("Name: ", name)
#     print("Age: ", age)


# print_info(age = 345, name = "Liubov")




# def sayHello(user_name: str, user_age: int = 0) -> str:
#     """
#     input parameters: None
#     output: str 
#     """
#     return f"Hello, {user_name}, age {user_age}"
    

# print(dir())
# print(sayHello.__doc__)
# print(sayHello("Liubov", 89))
# print(sayHello(34, 78))

# def print_info(name, age = 80):
#     print("Name: ", name)
#     print("Age: ", age)

# print_info("Alex")
# print("-" * 10)
# print_info(age = 90, name = "Sam")

# a = input("Enter your name:")
# b = input("Enter your age:")
# print_info(age = b, name = a)




# def sayHello():                
#    print('Hello world!')                                
# # # # ####################################3
  
# sayHello() 
# sayHello() 
#                          # викликаємо функцію

#########################################
# t=sayHello 
# print(t)                         # викликаємо функцію знову
#######################

# # ##
# def add(x, y):
#     return x + y
# # # # # ##
# # print(add.__doc__)

# # print(add(1, 10))

# # # # ##
# print(add('abc', 'def'))
# #

###################################
def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc
####################################
# new = newfunc(100)
# print(new(200))
# # # ###

#########################################
# def func():
#     pass
    
# ########################################## # # # #
# print(func())
#################################


############################################3
# # ###Якщо функція нічого 
# # # не повертає, а саме 
# # # не завершується словом
# # #return, то функція повертає 
# # #значення None
# # ###################################
# # #example function
# # ############################
# def my_function(argument):
#     print(argument)
# # #####################################


# my_function("abracadabra")
# # #############################

# print(my_function("abracadabra"))

# # ###################################################
# #Required arguments (обовязкові аргументи функції)
#######################################################
# def print_max(a, b):
#     if a > b:
#         print(a, 'is maximum')
#     elif a == b:
#         print(a, 'is equal to', b)
#     else:
#         print(b, 'is maximum')
 
# # # #Коректне використання функції

# print_max(3, 4)      #аргументи — літеральні константи
 


# # #Некоректне використання функції
# print_max()
# print_max(3)
# print_max(12,7,3)
# # 
# # ####################
# # #   
# x = 5
# y = 7
# print_max(x, y) #змінні як аргументи
####################################################

# # ##############################
# # #Аргументи функції,
# # #Типові значення аргументів
# # ##############################
# def say(message, times = 1):
#     print(message * times)
# # # # # # #
# say('Hello')
# # # # # #
# say('World', 5)
# # ########################
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
# # # 
# func(3, 7)
# #
# func(25, c=24)
# # #
# func(c=50, a=100)
# func(b=50, c=100)
# # #
# # ############################
# # # c - необовязковий аргумент
def func(a, b, c=2): 
    return a + b + c
###
# (func(1, 2))
# # # ####
# print(func(1, 2, 3))
# # ###
# # func(a=1, b=3)
# # ##
# # func(a=3, c=6) #b не визначений, Error
# # ###########################################

# # # def func(a, b=5) правильно

# # func(a=5, b) #неправильно
#############################################
# # # Тільки ті параметри, які знаходяться 
# # # в кінці списку параметрів можуть 
# # # мати типові значення. 
# # ##############################################


######################################################
# # #Keyword argument (аргументи-ключові слова)
#######################################################

# def person(name, age):
#     print(name, "is", age, "years old")
# # #
# def person(name, age=25):
#     print(name, "is", age, "years old")
# person(name="John", age=35)
# # # # #
# person(age=23, name="John")

######################################################
# # #Default argument аргументи задані по замовчуванню
########################################################

# def space(planet_name, center="Star"):
#     print(planet_name, "is orbiting a", center)
# #
# space("Mars")
# #
# space("Mars", "Black Hole")

# # #########################################################
# # # Variable-length arguments аргумент довільної довжини
############################################################

# def unknown(name, *args):
#     print("name", name)
#     print(type(args),args)
#     for argument in args:
#         print(argument)
 
# # # # # # # # # # #  ################
# unknown("hello","world")
# unknown(1, 2, 3, 4, 5) 
# unknown()

###############################

# # #довільна кількість неіменованих аргументів
# # # args це кортеж
def func(*args):
    # print(type(args))
    for item in args:
        print(item)
    return args
# # # # #
# print(func(1, 2, 3, 'abc'))
# # # ###
# print(func(678))
# # # ##
# print(func(1))
################################
# # #довільна кількість іменованих аргументів
# # #змінна kwargs це словник 
################################################

def func(**kwargs):
    print(type(kwargs), kwargs)
    return kwargs
# # # # # # # # # # # ###
# w = func(a = 1, b = 2, c = 3)
# print(w)
# # # # # # # ###
# t=func()
# print(t)
# ##
# w=func(a='python')
# print(w)
# # # ###



#######################################
# # #Лямбда функція (анонімна функція)
########################################


def f(x):
    return x**2

# # # # # # # # # # # # # ####
# print(f(4))
# # # # # # # ####

# print((lambda x: x**2)(3))

# g = lambda x: x**2


# print(g) 
# g(5) 
# # # # # # # # # # # # #
# print(g(3))
# # # # # #


# print((lambda x: x**2)(5))

# # #######
# func = lambda x, y: x + y
# # # # # # # #####
# print(func(1, 2))
# # # # ######
# print(func('a', 'b'))
# # # ######
# print((lambda x, y: x + y)(1, 2))
# # # #####
# print(lambda x, y: x + y)('a', 'b')
# # #####
# # #Лямбда функція не потребує return
# func = lambda *args: args
# # # # ####
# print(func(1, 2, 3, 4))
# # #######################################
# # map
# # ##################################
# # #Списки можна обробляти lambda-функціями 
# # # всередині інших функцій, наприклад 
# # # таких функцій як map(), filter(), reduce()
#################################################

# # #######Глобальна змінна

# # # глобальна змінна age
age = 44
 
# def info():
#     print(age) # Друкуєм глобальну змінну age
#  # створюєм локальну змінну age 
# def local_info():
#     age = 22  
#     print(age)

# info() 
# # print("###########")
# local_info() 
# # # ######################

# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)

# func(x)
# print('x is still', x)

# # #####
# # оператор global
# # глобальна змінна age
# age = 13
 
# # # функція яка змінює глобальну змінну
# def get_older():
#     global age
#     age += 1
 
# print(age) # надрукує 13
# get_older() # збільшуєм age на 1
# print(age) # надрукує 14
# # #############################
# # #####
# # # оператор nonlocal
# # #############################
# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer
# # # #
# c = counter()
# print(c()) #1
# print(c()) #2
# print(c()) #3
# print(c()) #4


# def f5(name,*args):
#     for var in args:
#         print(var)
#     print(type(args),type(name))
#     print(args)
#     print(name)

# list1=["red", "red", "black"]

# def ff(x):
#     return x == "red"

# d = list(filter(ff, list1))
# print(d)

# def my_print(name_user):
#     """
#     name function:         my_print
#     type input parameter : str
#     output:                None
#     """
#     print(f"Hello, {name_user}")
#     return f"Hello, {name_user}"
#     print("after")

# a = my_print("Volodymyr")
# print(a)


# print(my_print.__doc__)

# def my_sum(arg1 = 45, arg2 = 67):
#     total = arg1 + arg2
#     return total
    


# print(my_sum())

# def print_info(**kwargs):
#   #  print("arg1: ", type(arg1), arg1)
#      print("args", type(kwargs), kwargs)


# print_info()
