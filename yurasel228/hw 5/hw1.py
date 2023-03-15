List_int = [1, 2, 3, 4, 5, 6, 7]

float_list= []
for num in List_int:
    float_num = float(num)
    float_list.append(float_num)

print(f"int : {List_int}")
print(f"float : {float_list}")