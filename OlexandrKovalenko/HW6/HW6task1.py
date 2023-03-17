list=[1,2,3,4,5,6,7,8,9,10]
l1=len(list)

div2 = [list[i] for i in range(0,l1) if list[i]%2==0]
# div2 = []
# for i in range(0,l1):
#   if list[i]%2==0:
#     div2.append(list[i])

print ("Even numbers that are divisible by 2: ", div2)

div3 = [list[i] for i in range(0,l1) if list[i]%3==0 and list[i]%2!=0]
# div3 = []
# for i in range(0,l1):
#   if list[i]%3==0 and list[i]%2!=0:
#     div3.append(list[i])

print ("Odd numbers, which are divisible by 3: ", div3)

notdiv2and3 = [list[i] for i in range(0,l1) if list[i]%3!=0 and list[i]%2!=0]
# notdiv2and3 = []
# for i in range(0,l1):
#   if list[i]%3!=0 and list[i]%2!=0:
#     notdiv2and3.append(list[i])

print ("Numbers that are not divisible by 2 and 3: ", notdiv2and3)
