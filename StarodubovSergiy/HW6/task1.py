# In the range from 1 to 10 determine
# - even numbers that are divisible by 2,
# - odd numbers, which are divisible by 3,
# - numbers that are not divisible by 2 and 3

divisible_2 = []
divisible_3 = []
not_divisible_2_and_3 = []

for i in range(1,10):
   if i%2==0:
      divisible_2.append(i)

for i in range(1,10):
   if i%3==0 and i%2!=0:
      divisible_3.append(i)

for i in range(1,10):   
    if i%2!=0 and i%3!=0:
      not_divisible_2_and_3.append(i)

print("The numbers divisible by 2 is: ", divisible_2)
print("The numbers divisible by 3 is: ", divisible_3)
print("The numbers divisible by 2 and 3 is: ", not_divisible_2_and_3)