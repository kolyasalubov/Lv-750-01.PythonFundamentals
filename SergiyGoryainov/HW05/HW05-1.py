# Create a list that contains elements of integer type,
# use the loop to change elements to floating type

int_to_float_list = list(range(10))
for element in range(len(int_to_float_list)):
    int_to_float_list[element] = float(int_to_float_list[element])

print(int_to_float_list)
print(type(int_to_float_list[element]))


