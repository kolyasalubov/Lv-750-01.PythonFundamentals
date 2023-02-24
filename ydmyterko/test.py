# if False:
#     print("Nissan")
# elif True:
#     print("Ford")
# else:
#     print("Audi")


# a, b = 12, 5
# if a + b:
#     print('True')
# else:
#     print('False')

# x = 0
# a = 0
# b = -5
# if a > 0:
#     if b < 0: 
#         x = x + 5 
#     elif a > 5:
#         x = x + 4
#     else:
#         x = x + 3
# else:
#     x = x + 2
# print(x)

# x = 100
# y = 50
# print(x and y)


# if 2 == 2:
#     print("ice cream is tasty!")

# if -3

#str1 = "-100"
#print(str1.isdigit())


# word = "1111111111119999"
# updated = word[12:16]
# print(updated)
# print(len(word))

# if len(word)<16:
#     result="Invlid card"
# else:
#     result = "****" + word[12:16]
# print(result)




str = 'programiz' 
# print('str = ', str)
# #first character 
# print('str[0] = ', str[0])
# #last character 
# print('str[-1] = ', str[-1])
# #slicing 2nd to 5th character 
#print('str[1:5] = ', str[1:5])
# #slicing 6th to 2nd last character 
# print('str[5:-2] = ', str[5:-1])

# str1 = "Test"
# for i in str1:
#     print(i)

# number = "100"
# for i in number:
#     if i==0:
#         result=False
#     else:
#         result=True
#     print(i)
# print(result)

# word="PasSword"
# result=True
# for i in word:
#     print(i)
#     print(word.count(i))
#     if word.count(i)>1:
#         result=False
#         break

# sum=0
# n = 123
# while(n!=0):
#     sum=sum+n%10
#     print(n%10)
#     n=n//10
#     print(n)
# print(sum)

# binary1='101'
# print(binary1)

# decimal=0
# pos=len(binary1)

# for i in binary1:
#     print(i)
#     decimal = decimal + int(i)*2**pos
#     pos-=1
#     print(decimal)
#     print(pos)
#     print('')

# print(decimal)

# binary=''
# n=0

# while n==0:
#     digit=n%2
#     #binary=str(digit) + binary
#     n=n//2
#     print(n)
#     print(digit)
#     print('')


# binary_number="011"
# list_result=[]
# for i in binary_number:
#     print(i)
#     if i=='1':
#         list_result.append(True)
#     else:
#         list_result.append("False")

# print(list_result)


# var = 10
# for i in range(10):
#     print("i=", i)
#     for j in range(2, 10, 1):
#         print("j=", j)
#         if var % 2 == 0:
#             continue
#             var += 1
#         print('var j', var)
#     var+=1
#     print(var)
#     print('')
# else:
#     var+=1
# print(var)


# for num in range(2,-5,-1):
#     print(num, end=", ")


# numbers = [10, 20]
# items = ["Chair", "Table"]

# for x in numbers:
#   for y in items:
#     print(x, y)


# x = 0
# while (x < 100):
#   x+=2
# print(x)


for num in range(10, 14):
    print('')
    print(num)
   for i in range(2, num):
    #print(i)
    if num%i == 1:
        print(num)
        break




