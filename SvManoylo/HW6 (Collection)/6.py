# #Task 1
# def operation_with_range(range):
#     even_list = []
#     odd_list = []
#     not_divisible_number = []
#     for number in set(range):
#         if number == 0:
#             print("0 is not divisible")
#         elif number % 2 == 0:
#             even_list.append(number)
#         elif number % 3 == 0 and number not in even_list:
#             odd_list.append(number) 
#             print("Odd number ", odd_list)
#             print ("Even number ", even_list)
#         else:
#             not_divisible_number.append(number)
#             print ("Number ", not_divisible_number, " are not divisible 2 or 3") 
#     return even_list, odd_list, not_divisible_number

# range = (2, 5, 6, 9, 0)
# a = operation_with_range(range)

# #Task 2
# username = input("Username ", )
# while True:
#     if username == "First":
#         print(f"Hello {username}!")
#         break
#     else:
#         print("Invalid username")
#         username = input("Check username")
   
def add_indexes(lst):
    new_lst = []
    for i in range(len(lst)):
       i = list(i) + lst[i]
       new_lst.append(i)
       return new_lst


lst = (2, 5, 3, 0)
a = add_indexes(lst)
print(a)
