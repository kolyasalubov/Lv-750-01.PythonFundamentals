# Create a list that contains elements of integer type, 
# then use the loop to change the type of these elements to a floating type. 
# (Hint: use the built-in float () function)

my_list = [1, 5, 15, 33, 85]

float_list = []
for i in my_list:
    converted_number = float(i)
    float_list.append(converted_number)