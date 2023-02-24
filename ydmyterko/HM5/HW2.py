number = int(input("Please enter a number bigger then 1: "))
print(f"Your number is {number}")
fibonachi_list=[0,1]

num_prev1=0
num_prev2=1
num_curr=0
num_next=0
while num_prev1+num_prev2<=number:
    num_curr=num_prev1+num_prev2
    fibonachi_list.append(num_curr)

    num_prev1=num_prev2
    num_prev2=num_curr
    num_next=num_prev1+num_prev2

print('Fibonachi list:', fibonachi_list)

