number = int(input("Please enter a number bigger then 1: "))
print(f"Your number is {number}")
fibonachi_list=[0,1]

num_p1=0
num_p2=1
num_c=0
num_next=0
while num_p1+num_p2<=number:
    num_c=num_p1+num_p2
    fibonachi_list.append(num_c)

    num_p1=num_p2
    num_p2=num_c
    num_next=num_p1+num_p2

print('Fibonachi list:', fibonachi_list)