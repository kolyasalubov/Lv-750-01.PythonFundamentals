list_int = [12, 13, 20, 30]
float_list = []
for i in list_int:
    float_list.append(float(i))
    i = i + 1
print(float_list)