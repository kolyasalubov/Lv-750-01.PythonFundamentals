entered_number = int(input("Enter your number to make Fibonacci nummber:"))
n1 = 0
n2 = 1
count = 0
if entered_number <= 0:
    print("Please, enter positive integer.")
elif entered_number == 1:
    print("Your Fibonacci sequance times",entered_number,":")
    print(n1)    
else:
        
    while count < entered_number:
        print(n1)
        next_n = n1 + n2
        n1 = n2
        n2 = next_n 
        count += 1
    