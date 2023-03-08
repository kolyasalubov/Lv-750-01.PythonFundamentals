amount = int(input('Amount?'))
element_list = [int(input('Уведи число')) for item in range(amount)]
for item in range(amount):
    element_list[item] = float(element_list[item])
print('You are creator of {} elements list and your floated list is {}'.format(amount,element_list))