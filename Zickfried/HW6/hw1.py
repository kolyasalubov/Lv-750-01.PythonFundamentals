#determining even numbers that are divisible by 2
first_list = []
second_list = []
third_list = []
for i in range(10):
    if i % 2 == 0:
        first_list.append(i)
print("These are even numbers that are divisible by 2:{}".format(first_list))

#determining odd numbers, which are divisible by 3  
      
for j in range(10):  
    if j % 3 == 0:
        second_list.append(j)
print(f"These are odd numbers, which are divisible by 3:{second_list}") 
            
#numbers that are not divisible by 2 and 3

for v in range(10):
    if v % 2 != 0 and v % 3 != 0:
        third_list.append(v)
print(f"These are numbers that are not divisible by 2 and 3:{third_list}")        
        