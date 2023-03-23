# days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# print("1-7 corresponds Monday-Sunday")
# try:
#     user_input = int(input("Enter number of a day 1-7: "))

#     if user_input in range(1,7):
#         print(days[user_input]) 
# except ValueError as e:
#     print(e)       
                
days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}

try:
    user_input = int(input("Enter number of day 1-7:"))
    
    if user_input in days:
        print(days[user_input])
    else:
        print("Invalid input. Please enter a number between 1 and 7.")
        
except ValueError as e:
    print(e)    