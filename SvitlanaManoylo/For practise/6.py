# x = ["apple", 
#      "banana", 
#      "cherry"]

# print(dict(enumerate(x)))

# pow2 = []

# for x in range(10):
#     if x%2 == 0:
#         pow2.append(2**x)

# print(pow2)


# pow3 = [2**x for x in range(10) if x%2 == 0]
# print(pow3)






# r = [7,8,9]
# print(r.append(555))
# print(r)
# r = [44,18,9,789]
# print(r.sort(),r)
# r1 = [78, 556, 23, 2]
# print(r1.append(598))
# print(sorted(r1),r1)
# ################################
# pow2 = []
# for x in range(10):
#     if x % 2==0:
#         pow2.append(2 ** x)
# print(pow2)
##########################

# pow3 = [2**item for item in range(10) if item % 2==0] 
# print(pow3)


### List
###############################

# value=[1,5,8,9]
# print(value)

# #############################
# value=[1,5,8,9]
# print(value[0])
# print(value[11])   # Index Error

# ##############################
# value=[1,5,8,9]
# value.append(56)
# print(value)

# #############################
# value=[1,5,8,9]
# value.append([7,9,33])
# value.extend([7,9,33])
# print(value)
# print(value[4][0])

#########################
#!!!!!!!!!!!!!!!!!!!!!
#########################

# value=(1,5,8,9,[4,5,7])
# value[4][0]=99
# print(value)


# ##############################
# this_list = ["apple", "banana", "cherry"]
# this_list.append("orange")
# print(this_list)

# ###########################
# value=[1,5,8,9]
# value.insert(2,20)
# print(value)

# ########################
# this_list = ["apple", "banana", "cherry","banana","lemon"]
# this_list.remove("banana")
# print(this_list)

# ######################
# this_list = ["apple", "banana", "cherry"]
# this_list.insert(1, "orange")
# print(this_list)


# ##########################
# value=[1,9,8,3,11]
# value.sort()
# print(value)

# #######################
# value=[1,9,25,8,3,11]
# y=value.pop()            #якщо індекс не вказаний видаляє 
# # #                        #ост. елем. списку і повертає його
# print(value)
# print(y)
######################
# print(value)
# print(value.pop(3))
# ################
# this_list = ["apple", "banana", "cherry"]
# this_list.pop()
# print(this_list)

# ####################
# value=[1,9,25,8,3,11]
# value.pop(3)
# #
# print(value)

# #########################3
# this_list = ["apple", "banana", "cherry"]
# print(this_list,id(this_list))
# del this_list[0]
# print(this_list,id(this_list))
# ########################3
# delete all list
#############################
# thislist = ["apple", "banana", "cherry"]
# print(id(thislist)) 
# del thislist
# print(id(thislist))                #this will cause an error 
#                                #because "thislist" no longer exists.
# #########################
# # clear() is the method empties the list
##############################
# this_list = ["apple", "banana", "cherry"]
# print(this_list,id(this_list))
# this_list.clear()
# print(this_list,id(this_list))


# #######################

# value.sort()
# print(value)
# #########################
# #copy
# ###
a = [1, 7, 9,[8,9]]
b = a.copy()
# print(a,id(a))
# print(b,id(b))
# # # #####################
# print(a,id(a[3]))
# print(b,id(b[3]))

# ############################
# #the list() constructor
# ###########################

# this_list = list(("apple", "banana", "cherry"))       # note the double round-brackets
# print(this_list)

# ##################
# ### Tuple
# ##################

# value=(7,9,3,6)
# print(value)

# ################

# value[2]

# ###################

# value=(7,8,3,5)
# print (("bat","led")+value)


# ###################
# value=(7,8,3,5)
# # value[1]=7   # Exception
# print(value[0:2])

# ##################
# Tuple не підтримує 
# транзитивність стосовно
# immutable
# t=(2,8,[6,7])

# ##############################
# ### Dictionary
# ###########################3

# dict_number={"key1":1,"key2":2}
# print(dict_number)

# #########################
# dict_number["key1"]

# #####################

# dict_number={"key1":1,"key2":2}
# # # dict_number["ball"]  # KeyError

# # #print(dict_number.get("ball"))  # None
# # # #
# # # ###############

# dict_number["key3"]=3

# print(dict_number)

# # ########################3

# dict_number.update({"key3":333})
# print(dict_number)

# # #######################

# # dict_number.keys()

# ######################

# dict_number.values()

# ###############

# dict_number.items()

# #########################

# dict_number.pop("key1")
# # витирає запис з даним 
# # ключем і повертає значення, 
# # яке відповідає даному ключу  

######################
# #Set
######################


# set_number={1,5,8,8,8}
# print(set_number)

# ####

# set_number = {1,1.2,2,2,2,2,7,9,4}

# # #######

# set_number.add(4)
# print(set_number)

# #оскільки множина 
# # як і дікт невпорядкована, то
# # не факт, що 4 потрапить в кінець множини
# # 
# #перетин множин
# set_number&{3,4,5}
# print(set_number) 

# ################
# #об'єднання множин

# set_number | {3,4,5}

# ####################3
# myset-{4,3,2}

###########
# #Slices
###########

# data=(1,2,34,6,7)
# for x in data[::-1]:
#     print(x)

# l=[6,8,9,44]
# k=l
# print(k,id(k))
# print(l,id(l))
# z=l[0:4]
# print(z,id(z))
# l.append(55)
# print(l,k,z)


# l1=[56,3,2,90]
# l2=[9,3,5,7]
# print("before sort", l1)
# p = l1.sort()
# print("p", p)
# print("after sort",l1)
# print("before sorted", l2)
# t = sorted(l2)
# print("after sorted", l2)
# print("t", t)

# my_list=["red", "black", "white"]
# u = enumerate(my_list,45)
# print(u)
# for value in u:
#     print(value)

# r = (67,5,34)
# w = list(r)
# print(w, id(w))
# print(r, id(r))