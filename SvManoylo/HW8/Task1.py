
print ("Addition - 1")
print ("Subtraction - 2")
print ("Multiplication - 3")
print ("Division - 4")

i = int(input("Choose operation - "))
num_1 = int(input("First digit "))
num_2 = int(input("Second digit "))

def calc(i): 
        if i == 1:
            result = num_1 + num_2
            print(f"{num_1} addition by {num_2} is {result}")
        elif i == 2:
            result = (num_1 - num_2)
            print(f"{num_1} subtraction by {num_2} is {result}")
        elif i == 3:
            result = (num_1 * num_2)
            print(f"{num_1} multiplication by {num_2} is {result}")
        elif i == 4:
            result = (num_1 / num_2)
            print(f"{num_1} subtraction by {num_2} is {result}")
        else: 
            print("Choose again")
        return i

calc(i)
print(__name__)