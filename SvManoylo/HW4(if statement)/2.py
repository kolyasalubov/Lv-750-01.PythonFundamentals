# #1 task
# a = int(input ("Add you number a"))
# b = int(input ("Add you number b"))
# if a > b:
#     print (('Your number'), a, ('>'), b)
# elif a < b:
#     print (('Your number'), a, ('<'), b)
# else: 
#     print ("yor numder is Null")

# #2 task

# a = int(input ("Add you number a"))
# if a % 2 == 0:
#     print ('Your number is eval')
# else:
#     print ('Your number is odd')

# #3 task
# x= int(input('Your number '))
# fact=1 
# for i in range(1,x+1): 
#     fact=fact*i 
#     print("The factorial of ", x," is: ",fact)



def card_hide(card):
    card = int(input('your number'))
    card_hide1 = str((card)[12:17])
    last_numbers = int(card_hide1)
    print ('************', last_numbers)
    if str(card_hide(16)):
        return "Ivalid card"